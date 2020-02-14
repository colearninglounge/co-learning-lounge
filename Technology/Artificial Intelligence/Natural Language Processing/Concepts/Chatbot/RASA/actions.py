# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
import ast
from rasa_sdk.events import SlotSet


class BingLocationExtractor:
    
    def __init__(self):
       self.bing_baseurl="http://dev.virtualearth.net/REST/v1/Locations"
       self.bing_api_key="AmLh1M2aXvCGrc3c2AxuqcttZvc2jVTYOvGjjbL7RwM7F-zBVNPEg696TtAlh0Mr" ## Update Bing API key here

    def getLocationInfo(self, query, tracker):
        
       list_cities=[]
       queryString = {
                        "query":query,
                        "key":self.bing_api_key
                     }
       res = requests.get(self.bing_baseurl,params=queryString)

       res_data = res.json()
       
       if (res.status_code != 200 or "low" == (res_data["resourceSets"][0]["resources"][0]["confidence"]).lower()) :
           return None, None
       else:
           if ("locality" in res_data["resourceSets"][0]["resources"][0]["address"]) :
            return res_data["resourceSets"][0]["resources"][0]["address"]["locality"], res_data["resourceSets"][0]["resources"][0]["name"]
           else :
            return "that", res_data["resourceSets"][0]["resources"][0]["name"]

class ActionSetLocation(Action):


    def name(self):
        return "action_set_location"

    def run(self, dispatcher,tracker, domain):

        user_input = tracker.latest_message['text']

        le = BingLocationExtractor()
        locality, location_name = le.getLocationInfo(str(user_input), tracker)

        dispatcher.utter_message("Thanks for sharing you location. " + locality.capitalize() + " is pretty place.")
        return [SlotSet("location",location_name)]

class Zomato:

    def __init__(self):
        self.api_key="a7e3c34603ce43509e9f1a1c606c0bc2"  ## Update Zomato API key here
        self.base_url = "https://developers.zomato.com/api/v2.1/"


    def getZomatoLocationInfo(self, location):
        '''
        Takes city name as argument.
        Returns the corressponding city_id.
        '''
        #list storing latitude,longitude...
        location_info=[]

        queryString = { "query" : location }

        headers = {'Accept': 'application/json', 'user-key': self.api_key}

        res = requests.get(self.base_url+"locations", params=queryString, headers=headers)

        data = res.json()

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

        queryString = { 
                        "lat":location_info[0],
                        "lon":location_info[1]
                        }

        res = (requests.get(self.base_url +"cuisines",params=queryString,headers=headers).content).decode("utf-8")

        a = ast.literal_eval(res)
        all_cuisines_in_a_city = a['cuisines']

        cuisines={}

        for cuisine in all_cuisines_in_a_city:
            current_cuisine = cuisine['cuisine']
            cuisines[current_cuisine['cuisine_name'].lower()] = current_cuisine['cuisine_id']

        return cuisines


    def get_cuisine_id(self, cuisine_name, location_info):
        '''
        Takes cuisine name and city id as argument.
        Returns the cuisine id for that cuisine.
        '''
        cuisines = self.get_cuisines(location_info)

        return cuisines[cuisine_name.lower()]


    def get_all_restraunts(self, location, cuisine):
        '''
        Takes city name and cuisine name as arguments.
        Returns a list of 5 restaurants.
        '''

        location_info = self.getZomatoLocationInfo(location)
        cuisine_id = self.get_cuisine_id(cuisine,location_info)

        queryString = { 
                        "entity_type":location_info[3], 
                        "entity_id":location_info[2], 
                        "cuisines":cuisine_id, 
                        "count":5
                        }

        headers = {'Accept': 'application/json', 'user-key': self.api_key}
        res = requests.get(self.base_url + "search",params=queryString, headers=headers)

        list_of_all_rest=res.json()["restaurants"]

        names_of_all_rest=[]
        for rest in list_of_all_rest:
            names_of_all_rest.append(rest["restaurant"]["name"])

        return names_of_all_rest

    def get_all_restraunts_without_cuisne(self, location):
        '''
        Takes city name as arguments.
        Returns a list of 5 restaurants.
        '''

        location_info = self.getZomatoLocationInfo(location)

        queryString = {
                        "entity_type": location_info[3],
                        "entity_id": location_info[2],
                        "count": 5
                        }

        headers = {'Accept': 'application/json', 'user-key': self.api_key}
        res = requests.get(self.base_url + "search", params=queryString, headers=headers)

        list_ofall_rest = res.json()["restaurants"]
        names_of_all_rest = []
        for rest in list_ofall_rest:
            names_of_all_rest.append(rest["restaurant"]["name"])

        return names_of_all_rest


class GetRestaurantsWithoutCuisine(Action):

    def name(self):
        return "action_restaurants_nocuisine"

    def run(self, dispatcher, tracker, domain):
        location_name = tracker.get_slot('location')

        zo = Zomato()

        list_all_restaurants = zo.get_all_restraunts_without_cuisne(str(location_name))

        temp_str = ""

        for r in range(0, len(list_all_restaurants) - 1):
            temp_str = temp_str + str(list_all_restaurants[r]) + ", "

        temp_str = temp_str + "and " + str(list_all_restaurants[-1])

        dispatcher.utter_message("We found " + str(temp_str) + " at " + location_name[1] + " location. Have a great time :)")

        return []

class ActionShowRestaurants(Action):

    def name(self):
        return "action_show_restaurants"

    def run(self, dispatcher,tracker,domain):

        user_input = tracker.latest_message['text']

        zo = Zomato()

        ## Extracting location either from "location" slot or user input
        le = BingLocationExtractor()
        location_name = tracker.get_slot('location')
        if (not location_name) :
            locality, location_name = le.getLocationInfo(str(user_input), tracker)

        if not location_name :
            ### Utter template
            dispatcher.utter_template('utter_ask_location', tracker)
        else:
            cuisine_type = tracker.get_slot('cuisine')
            list_all_restaurants = zo.get_all_restraunts(location=location_name, cuisine=str(cuisine_type))
            temp_str = ""

            if (list_all_restaurants) :
                for r in range(0,len(list_all_restaurants)-1):
                	temp_str = temp_str + str(list_all_restaurants[r]) + ", "

                temp_str = temp_str + "and " + str(list_all_restaurants[-1])

                dispatcher.utter_message("We found " + str(temp_str) + " of " + cuisine_type.capitalize() + " cuisine at "+ location_name +" location. Have a great time :)")
            else :
                dispatcher.utter_message("Sorry no such restaurant of " + cuisine_type.capitalize() + " available at " + location_name + ". Try looking for some other cuisine.")

        return []
