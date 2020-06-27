# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


from typing import Any, Text, Dict, List, Union, Optional
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
import ast
from rasa_sdk.events import SlotSet
from rasa_sdk.forms import FormAction
import time


class RestaurantForm(FormAction):
    """Example of a custom form action"""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "restaurant_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["num_people", "phone_num", "time"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "num_people": [
                self.from_entity(entity="number", intent=["telling_numpeople"]),

            ],
            "phone_num": [
                self.from_entity(entity="number", intent=["telling_phonenum"]),

            ],
            "time": [
                self.from_entity(entity="time", intent=["telling_datetime"]),

            ],
        }

    def validate_phone_num(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate cuisine value."""

        if len(str(value)) == 10:
            # validation succeeded, set the value of the "cuisine" slot to value
            return {"phone_num": value}
        else:
            dispatcher.utter_message(template="utter_invalid_phone_num")
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"phone_num": None}

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        dispatcher.utter_template(template="utter_submit", tracker=Tracker)
        return []


class ActionGetDateTime(Action):
    def name(self):
        return 'action_get_date_time'


    def run(self, dispatcher, tracker, domain):
        temp = tracker.get_slot('time')

        slots = []

        data = temp[:-10]

        temps = time.strptime(data, "%Y-%m-%dT%H:%M:%S")
        date_slot = time.strftime("%d/%m/%Y", temps)
        time_slot = time.strftime("%H:%M", temps)

        slots.append(SlotSet("date_slot", date_slot))
        slots.append(SlotSet("time_slot", time_slot))

        return slots


class BingLocationExtractor:

    def __init__(self):
        self.bing_baseurl = "http://dev.virtualearth.net/REST/v1/Locations"
        self.bing_api_key = "AmLh1M2aXvCGrc3c2AxuqcttZvc2jVTYOvGjjbL7RwM7F-zBVNPEg696TtAlh0Mr"  # Update Bing API key here

    def getLocationInfo(self, query, tracker):

        list_cities = []
        queryString = {
            "query": query,
            "key": self.bing_api_key
        }
        res = requests.get(self.bing_baseurl, params=queryString)

        res_data = res.json()

        if res.status_code != 200 or "low" == (res_data["resourceSets"][0]["resources"][0]["confidence"]).lower():
            return None, None
        else:
            if "locality" in res_data["resourceSets"][0]["resources"][0]["address"]:
                return res_data["resourceSets"][0]["resources"][0]["address"]["locality"], \
                       res_data["resourceSets"][0]["resources"][0]["name"]
            else:
                return "that", res_data["resourceSets"][0]["resources"][0]["name"]


class ActionSetLocation(Action):

    def name(self):
        return "action_set_location"

    def run(self, dispatcher, tracker, domain):
        user_input = tracker.latest_message['text']

        le = BingLocationExtractor()
        locality, location_name = le.getLocationInfo(str(user_input), tracker)

        dispatcher.utter_message(template="Thanks for sharing you location. " + locality.capitalize() + " is pretty place.")
        return [SlotSet("location", location_name)]


class BotGreet(Action):
    def name(self):
        return 'action_bot_greet'

    def run(self, dispatcher, tracker, domain):
        message = {
            "text": "Hey!! How are you..?I can help you to find restaurants based on your preferred "
                    "location and cuisine.",
            "quick_replies": [
                {
                    "content_type": "text",
                    "title": "I'm Hungry",
                    "payload": "/restaurant_search",
                }, {
                    "content_type": "text",
                    "title": "Nothing",
                    "payload": "/deny",
                }
            ]
        }

        dispatcher.utter_message(json_message=message)
        return []


class Zomato:

    def __init__(self):
        self.api_key = "a7e3c34603ce43509e9f1a1c606c0bc2"  # Update Zomato API key here
        self.base_url = "https://developers.zomato.com/api/v2.1/"

    def getZomatoLocationInfo(self, location):
        '''
        Takes city name as argument.
        Returns the corressponding city_id.
        '''
        # list storing latitude,longitude...
        location_info = []

        queryString = {"query": location}

        headers = {'Accept': 'application/json', 'user-key': self.api_key}

        res = requests.get(self.base_url + "locations", params=queryString, headers=headers)

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
            "lat": location_info[0],
            "lon": location_info[1]
        }

        res = requests.get(self.base_url + "cuisines", params=queryString, headers=headers).content.decode("utf-8")

        a = ast.literal_eval(res)
        all_cuisines_in_a_city = a['cuisines']

        cuisines = {}

        for cuisine in all_cuisines_in_a_city:
            current_cuisine = cuisine['cuisine']
            cuisines[current_cuisine['cuisine_name'].lower()] = current_cuisine['cuisine_id']

        return cuisines

    def get_cuisine_id(self, cuisine_name, location_info):
        """
        Takes cuisine name and city id as argument.
        Returns the cuisine id for that cuisine.
        """
        cuisines = self.get_cuisines(location_info)

        return cuisines[cuisine_name.lower()]

    def get_all_restraunts(self, location, cuisine):
        """
        Takes city name and cuisine name as arguments.
        Returns a list of 5 restaurants.
        """

        location_info = self.getZomatoLocationInfo(location)
        cuisine_id = self.get_cuisine_id(cuisine, location_info)

        queryString = {
            "entity_type": location_info[3],
            "entity_id": location_info[2],
            "cuisines": cuisine_id,
            "count": 5
        }

        headers = {'Accept': 'application/json', 'user-key': self.api_key}
        res = requests.get(self.base_url + "search", params=queryString, headers=headers)

        list_of_all_rest = res.json()["restaurants"]

        json = []
        for rest in list_of_all_rest:
            name = rest["restaurant"]["name"]
            thumb = rest["restaurant"]["thumb"]
            url = rest["restaurant"]["url"]
            json.append(name)
            json.append(thumb)
            json.append(url)


        return json

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
            name = rest["restaurant"]["name"]
            thumb = rest["restaurant"]["thumb"]
            url = rest["restaurant"]["url"]
            list_ofall_rest.append(name)
            list_ofall_rest.append(thumb)
            list_ofall_rest.append(url)

        return names_of_all_rest


class GetRestaurantsWithoutCuisine(Action):

    def name(self):
        return "action_restaurants_nocuisine"

    def run(self, dispatcher, tracker, domain):
        location_name = tracker.get_slot('location')

        zo = Zomato()

        list_all_restaurants = zo.get_all_restraunts_without_cuisne(str(location_name))

        if list_all_restaurants:
            findata = []
            for i in range(len(list_all_restaurants)):
                if i % 3 != 0:
                    continue

                mydata = {
                    "title": list_all_restaurants[i],
                    "image_url": list_all_restaurants[i + 1],
                    "subtitle": "I don't know anything about it",
                    "default_action": {
                        "type": "web_url",
                        "url": list_all_restaurants[i + 2],
                        "webview_height_ratio": "tall"
                    },
                    "buttons": [
                        {
                            "type": "web_url",
                            "url": list_all_restaurants[i + 2],
                            "title": "View Website"
                        }, {
                            "type": "postback",
                            "title": "Start Chatting",
                            "payload": "DEVELOPER_DEFINED_PAYLOAD"
                        }
                    ]
                }

                findata.append(mydata)

            message = {
                "attachment": {
                    "type": "template",
                    "payload": {
                        "template_type": "generic",
                        "elements": "{}".format(findata)
                    }
                }
            }

            dispatcher.utter_message(json_message=message)
        return []


class ActionShowRestaurants(Action):

    def name(self):
        return "action_show_restaurants"

    def run(self, dispatcher, tracker, domain):

        user_input = tracker.latest_message['text']

        zo = Zomato()

        # Extracting location either from "location" slot or user input
        le = BingLocationExtractor()
        location_name = tracker.get_slot('location')
        if not location_name:
            locality, location_name = le.getLocationInfo(str(user_input), tracker)

        if not location_name:
            # Utter template
            dispatcher.utter_template(template='utter_ask_location', tracker=tracker)
        else:
            cuisine_type = tracker.get_slot('cuisine')
            list_all_restaurants = zo.get_all_restraunts(location=location_name, cuisine=str(cuisine_type))

            if list_all_restaurants:
                finaldata = []
                for i in range(len(list_all_restaurants)):
                    if i % 3 != 0:
                        continue

                    mydata = {
                        "title": list_all_restaurants[i],
                        "image_url": list_all_restaurants[i + 1],
                        "subtitle": "I don't know anything about it",
                        "default_action": {
                            "type": "web_url",
                            "url": list_all_restaurants[i + 2],
                            "webview_height_ratio": "tall"
                        },
                        "buttons": [
                            {
                                "type": "web_url",
                                "url": list_all_restaurants[i + 2],
                                "title": "View Website"
                            }, {
                                "type": "postback",
                                "title": "Start Chatting",
                                "payload": "DEVELOPER_DEFINED_PAYLOAD"
                            }
                        ]
                    }

                    finaldata.append(mydata)

                message = {
                    "attachment": {
                        "type": "template",
                        "payload": {
                            "template_type": "generic",
                            "elements": "{}".format(finaldata)
                        }
                    }
                }

                dispatcher.utter_message(json_message=message)
            else:
                dispatcher.utter_message(template=
                    "Sorry no such restaurant of " + cuisine_type.capitalize() + " available at " + location_name + ". Try looking for some other cuisine.")

        return []
