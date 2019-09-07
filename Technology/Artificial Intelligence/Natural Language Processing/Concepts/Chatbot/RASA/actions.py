from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
import ast
from rasa_sdk.events import SlotSet
from rasa_sdk.events import UserUtteranceReverted

import requests
import ast


class Zomato:

    def __init__(self):
        self.api_key="797e936d8ac687c396be2fec2a356217"
        self.base_url = "https://developers.zomato.com/api/v2.1/"


    def getLocationInfo(self,location):
        '''
        Takes city name as argument.
        Returns the corressponding city_id.
        '''
        #list storing latitude,longitude...
        location_info=[]

        queryString={"query":location}

        headers = {'Accept': 'application/json', 'user-key': self.api_key}

        r = requests.get(self.base_url+"locations",params=queryString, headers=headers)

        data=r.json()

	## Yogesh: When does the location_suggestions are empty? I see when location is not valid it return empty list. First of all this condition should have been checked during Bing API
        if len(data['location_suggestions']) == 0:
            raise Exception('invalid_location')
            
        else:
            location_info.append(data["location_suggestions"][0]["latitude"])
            location_info.append(data["location_suggestions"][0]["longitude"])
            location_info.append(data["location_suggestions"][0]["entity_id"])
            location_info.append(data["location_suggestions"][0]["entity_type"])
            return location_info

    def get_cuisines(self, location_info):
        """
        Takes City ID as input.
        Returns dictionary of all cuisine names and their respective cuisine IDs in a given city.
        """


        headers = {'Accept': 'application/json', 'user-key': self.api_key}

        queryString={"lat":location_info[0],"lon":location_info[1]}

        r = (requests.get(self.base_url +"cuisines",params=queryString,headers=headers).content).decode("utf-8")

        a = ast.literal_eval(r)
        all_cuisines_in_a_city = a['cuisines']

        cuisines={}

        for cuisine in all_cuisines_in_a_city:
            current_cuisine = cuisine['cuisine']
            cuisines[current_cuisine['cuisine_name'].lower()] = current_cuisine['cuisine_id']

        return cuisines


    def get_cuisine_id(self,cuisine_name,location_info):
        '''
        Takes cuisine name and city id as argument.
        Returns the cuisine id for that cuisine.
        '''
        cusines = self.get_cuisines(location_info)

        return cusines[cuisine_name.lower()]


    def get_all_restraunts(self,location,cuisine):
        '''
        Takes city name and cuisine name as arguments.
        Returns a list of 5 restaurants.
        '''

        location_info=self.getLocationInfo(location)
        cuisine_id=self.get_cuisine_id(cuisine,location_info)

        queryString={"entity_type":location_info[3], "entity_id":location_info[2], "cuisines":cuisine_id, "count":5}

        headers = {'Accept': 'application/json', 'user-key': self.api_key}
        r = requests.get(self.base_url + "search",params=queryString, headers=headers)

        list_ofall_rest=r.json()["restaurants"]

        names_of_all_rest=[]
        for rest in list_ofall_rest:
            names_of_all_rest.append(rest["restaurant"]["name"])

        return names_of_all_rest

    def get_all_restraunts_without_cuisne(self,location):
        '''
        Takes city name as arguments.
        Returns a list of 5 restaurants.
        '''

        location_info=self.getLocationInfo(location)
        
        queryString={"entity_type":location_info[3],"entity_id":location_info[2],"count":5}

        headers = {'Accept': 'application/json', 'user-key': self.api_key}
        r =requests.get(self.base_url + "search",params=queryString, headers=headers)

        list_ofall_rest=r.json()["restaurants"]
        names_of_all_rest=[]
        for rest in list_ofall_rest:
            names_of_all_rest.append(rest["restaurant"]["name"])

        return names_of_all_rest



class LocationExtractor:
    
    def __init__(self):
       self.bing_baseurl="http://dev.virtualearth.net/REST/v1/Locations"
       self.bing_api_key="Aiw0X2IXCnSru_O00Rl8c8v6nULH-Z7r1HdFOVW3MQZEJoq6U2kQ_SVabSQui1GU"

    def getLocationInfo(self, query, tracker):
        
       list_cities=[]
       queryString={"query":query,"key":self.bing_api_key}
       r = requests.get(self.bing_baseurl,params=queryString)
       data = r.json()
       
       if (r.status_code != 200) :
           dispatcher.utter_template('utter_ask_location', tracker)
           return []
       else:
           return data["resourceSets"][0]["resources"][0]["point"]["coordinates"],data["resourceSets"][0]["resources"][0]["name"]

class ActionSetLocation(Action):


    def name(self):
        return "action_set_location"

    def run(self, dispatcher,tracker,domain):

        user_input=tracker.latest_message['text']

        le = LocationExtractor()
        location_name = le.getLocationInfo(str(user_input), tracker)

        return [SlotSet("location",location_name)]

		
class GetRestaurantsWithoutCuisine(Action):

    def name(self):
        return "action_restaurants_nocuisine"


    def run(self, dispatcher,tracker,domain):

        location_name=tracker.get_slot('location')
        
        zom = Zomato()

        list_all_restaurants = zom.get_all_restraunts_without_cuisne(str(location_name))
        
        temp_str = ""
        
        for r in range(0,len(list_all_restaurants)-1):
        	temp_str = temp_str + str(list_all_restaurants[r]) + ", "
        
        temp_str = temp_str + "and " + str(list_all_restaurants[-1])

        dispatcher.utter_message("We found " + str(temp_str) + " at " + location_name[1] +" location. Have a great time :)")

        return []




class ActionShowRestaurants(Action):

    def name(self):
        return "action_show_restaurants"

    def run(self, dispatcher,tracker,domain):

        zo = Zomato()
        le = LocationExtractor()
        user_input = tracker.latest_message['text']

        location_name = tracker.get_slot('location')
        if (not location_name) :
            location_name = le.getLocationInfo(str(user_input), tracker)

        if not location_name :
            ### Utter template
            dispatcher.utter_template('utter_ask_location', tracker)
        else:
            cuisine_type=tracker.get_slot('cuisine')
            list_all_restaurants=zo.get_all_restraunts(location_name[0],str(cuisine_type))
            temp_str = ""
            
            for r in range(0,len(list_all_restaurants)-1):
            	temp_str = temp_str + str(list_all_restaurants[r]) + ", "
            
            temp_str = temp_str + "and " + str(list_all_restaurants[-1])

            dispatcher.utter_message("We found " + str(temp_str) + " of " + cuisine_type + " cuisine at "+ location_name[1] +" location. Have a great time :)")

        return []
