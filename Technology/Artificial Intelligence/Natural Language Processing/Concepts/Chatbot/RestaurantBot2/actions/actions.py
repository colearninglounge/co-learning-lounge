# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
import ast
from rasa_sdk.events import SlotSet
from rasa_sdk.forms import FormAction
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

class BingLocation:

	def __init__(self):
		self.baseurl = "http://dev.virtualearth.net/REST/v1/Locations"
		self.bing_key = "AmAFc-8A6ubuUDQoWFKMF9EU335W20mAJTqBexfUqASF25iiWIBqjb5xc6RWooad"

	def getLocationInfo(self, query, tracker):

		list_cities = []
		queryString = {
			"query": query,
			"key": self.bing_key
		}

		result = requests.get(self.baseurl, params= queryString)

		if result.ok is False:
			return None, None
		else:
			data = result.json()
			print(data)
			if "locality" in data["resourceSets"][0]["resources"][0]["address"]:
				return data["resourceSets"][0]["resources"][0]["address"]["locality"], data["resourceSets"][0]["resources"][0]["name"]
			else:
				return data["resourceSets"][0]["resources"][0]["name"]


class SetLocation(Action):

	def name(self):
		return "action_set_location"

	def run(self, dispatcher, tracker, domain):
		user_input = tracker.latest_message['text']

		r = BingLocation()
		locality, location_name = r.getLocationInfo(str(user_input), tracker)

		dispatcher.utter_message(template="I've got your location: " + locality.capitalize())
		return [SlotSet("location", location_name)]


class Zomato:

	def __init__(self):
		self.baseurl = "https://developers.zomato.com/api/v2.1/"
		self.key = "8fbadec1470035c74baf9747b6b6b236"

	def getId(self, location):
		location_info = []

		queryString = {"query": location}
		headers = {'Accept': 'application/json', 'user-key': self.key}
		result = requests.get(self.baseurl + "locations", params = queryString, headers=headers)

		if result.ok is False:
			raise Exception('Invalid_location')

		else:
			data = result.json()
			location_info.append(data["location_suggestions"][0]["latitude"])
			location_info.append(data["location_suggestions"][0]["longitude"])
			location_info.append(data["location_suggestions"][0]["entity_id"])
			location_info.append(data["location_suggestions"][0]["entity_type"])
			return location_info


	def cuisines(self, location):

		headers = {'Accept': 'application/json', 'user-key': self.key}

		queryString = {
			"lat": location[0],
			"lon": location[1]
		}

		result = requests.get(self.baseurl + "cuisines", params=queryString, headers=headers).content.decode("utf-8")

		a = ast.literal_eval(result)
		all_cuisines = a['cuisines']

		res = {}

		for x in all_cuisines:
			i = x['cuisine']
			res[i['cuisine_name'].lower()] = i['cuisine_id']

		return res

	def cuisineId(self, cuisine, location):
		cuisines = self.cuisines(location)
		return cuisines[cuisine.lower()]

	def getRestaurants(self, location, cuisine):

		location = self.getId(location)
		cuisine_id = self.cuisineId(cuisine, location)

		queryString = {
			"entity_type": location[3],
			"entity_id": location[2],
			"cuisines": cuisine_id,
			"sort": "rating",
			"count": 3
		}

		headers = {'Accept': 'application/json', 'user-key': self.key}
		result = requests.get(self.baseurl + "search", params=queryString, headers=headers)

		all_restaurants = result.json()["restaurants"]

		l = []

		for x in all_restaurants:
			name = x["restaurant"]["name"]
			url = x["restaurant"]["url"]
			l.append(name)
			l.append(url)

		return l

	def getDefaultRestaurants(self, location):
		
		loc = self.getId(location)
		queryString = {
			"entity_id": loc[2],
			"entity_type": loc[3],
			"sort": "rating",
			"count": 3
		}

		headers = {'Accept': 'application/json', 'user-key': self.key}
		response = requests.get(self.baseurl + "search", params=queryString, headers=headers)

		x = []
		if response.ok is True:
			l = response.json()["restaurants"]
			for i in l:
				name = i["restaurant"]["name"]
				url = i["restaurant"]["url"]
				x.append(name)
				x.append(url)
		return x

class ActionShowRestaurants(Action):

	def name(self):
		return "action_show_restaurants"

	def run(self, dispatcher, tracker, domain):

		user_input = tracker.latest_message['text']

		z = Zomato()
		loc = BingLocation()
		location = tracker.get_slot('location')

		if not location:
			locality, location_name = loc.getLocationInfo(str(user_input), tracker)

		if not location:
			dispatcher.utter_template(template='utter_ask_location', tracker=tracker)
		else:
			cuisine_type = tracker.get_slot('cuisine')
			restaurantlist = z.getRestaurants(location=location, cuisine=str(cuisine_type))

			response = ""
			if restaurantlist:
				print(restaurantlist)
				for i in range(0, len(restaurantlist), 2):
					if i==len(restaurantlist):
						break
					
					response += restaurantlist[i]
					response += "\n" + restaurantlist[i+1]
					response += "\n\n"				
				print(response)	
				dispatcher.utter_template('utter_restaurants', tracker= tracker, response=response)

			else:
				dispatcher.utter_message(template= "I'm sorry, couldn't find restaurants." )

			return []

class ActionDefaultRestaurants(Action):

	def name(self):
		return "action_default_restaurants"

	def run(self, dispatcher, tracker, domain):
		location = tracker.get_slot('location')

		z = Zomato()

		l = z.getDefaultRestaurants(str(location))

		if l:
			response = ""
			for i in range(0, len(l), 2):
				if i==len(l):
					break
				response += l[i]
				response += "\n" + l[i+1]
				response += "\n\n"
			print(response)
			dispatcher.utter_template('utter_restaurants_noCuisine', tracker=tracker, response=response)
		else:
			dispatcher.utter_message(template= "I'm sorry, couldn't find restaurants." )

		return []

def valid_restaurant(resp, l):
	x = resp.split()
	temp = []
	"""for i in range(len(l)):
		if i%2==0:
			temp.append(l[i].lower())
		else:
			temp.append(l[i])"""
	common_words = ['i', 'a', 'the', 'these', 'an', 'am', 'tell', 'me', 'give', 'show', 'any', 'is', 'ah', 'um', 'that', 'like', 'are', 'at', 'ate']
	for i in range(len(x)):
		for j in range(len(l)):
			if j%2==0:
				if x[i].lower() in l[j].lower() and x[i].lower() not in common_words:
					return int(j)
	return -1

class ActionMenu(Action):

	def name(self):
		return "action_menu"

	def run(self, dispatcher, tracker, domain):
		location = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		if len(cuisine)>=1:
			resp = tracker.latest_message['text']
			final_response = ""
			z = Zomato()
			l = z.getRestaurants(location, cuisine)
			if (len(l)<2):
				l = z.getDefaultRestaurants(location)
			r = valid_restaurant(resp, l)
			if r>=0:
				if 'http' in l[r+1]:
					url = str(l[r+1])
					url = urljoin(url, urlparse(url).path)
					url += '/order'
					headers = {
					"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0"
					}
					response = requests.get(url, headers=headers)
					if response.ok:
						html = response.content
						soup = BeautifulSoup(html, "lxml")
						if len(soup.find_all('h4'))>0:
							if soup.find('div', class_='subtitle'):
								availability = soup.find('div', class_='subtitle').text
							else:
								availability = "Open now."
							final_response += availability + '\n\n'
							menu = soup.find_all('h4')
							menu_list = []
							temp_c = 0
							indexes = []
							i_temp = 0
							for a in menu:
								if "1hp8d8a" in str(a):
									temp_c = 1

								if temp_c==1:
									if "1hp8d8a" not in str(a):
										menu_list.append(a.text)
										temp_c = 0
										indexes.append(i_temp)

								if "1hp8d8a" not in str(a):
									i_temp += 1

							prices = soup.find_all('span', class_ = "sc-17hyc2s-1 fnhnBd")
							price_list = []
							i_temp = 0
							for a in prices:
								if i_temp in indexes:
									price_list.append(a.text)
								i_temp+=1
							l1 = len(menu_list)
							l2 = len(price_list)
							if (l1>l2):
								menu_list = menu_list[:l2]
								l1 = l2
							elif (l2>l1):
								price_list = price_list[:l1]
								l2 = l1
							for i in range(l1):
								final_response += menu_list[i] + ": " + price_list[i] + '\n'
						else:
							final_response += "Some fault, try something different perhaps?"  
					else:
						final_response += "Some fault, try something different perhaps?"
				else:
					final_response += "Server's making me sick! Try again later?"
			else:
				final_response += "Some fault, try something different perhaps?"
		else:
			final_response += "I didn't find menu. Please try again with proper name of restaurant! :)"
		dispatcher.utter_template('utter_menu', tracker=tracker, response=final_response)
		return []

class SetOrder(Action):

	def name(self):
		return "action_set_order"

	def run(self, dispatcher, tracker, domain):
		order = tracker.latest_message['text']
		dispatcher.utter_message(template="I've got your order: " + order)
		return [SlotSet("order", order)]

class SetAddress(Action):
	def name(self):
		return "action_set_address"

	def run(self, dispatcher, tracker, domain):
		address = tracker.latest_message['text']
		dispatcher.utter_message(template="I've got your address: " + address)
		return [SlotSet("address", address)]

class SetContact(Action):
	def name(self):
		return "action_set_contact"

	def run(self, dispatcher, tracker, domain):
		contact = tracker.latest_message['text']
		dispatcher.utter_message(template="I've got your contact number as: " + contact)
		if (str(contact).isdecimal() is True) and (len(contact)>=10 and len(contact)<=13):
			return [SlotSet("contact", contact)]
		else:
			return [SlotSet("contact", "Wrong Contact entered")]

class AskConfirm(Action):
	def name(self):
		return "action_ask_confirm"

	def run(self, dispatcher, tracker, domain):
		order = tracker.get_slot('order')
		address = tracker.get_slot('address')
		contact = tracker.get_slot('contact')
		response = "Your Order: " + str(order) + "\n" + "Address: " + str(address) + "\n" + "Contact No.:" + str(contact)
		dispatcher.utter_template('utter_confirm_order', tracker=tracker, response=response)
		return []
