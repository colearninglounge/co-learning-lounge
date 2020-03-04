import requests
import ast
import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class BingLocationExtractor:

    def __init__(self):
        self.bing_baseurl = "http://dev.virtualearth.net/REST/v1/Locations"
        self.bing_api_key = "AmLh1M2aXvCGrc3c2AxuqcttZvc2jVTYOvGjjbL7RwM7F-zBVNPEg696TtAlh0Mr"  ## Update Bing API key here

    def getLocationInfo(self, query):

        list_cities = []
        queryString = {
            "query": query,
            "key": self.bing_api_key
        }
        res = requests.get(self.bing_baseurl, params=queryString)

        res_data = res.json()
        logger.info(str(res_data))
        if res.status_code != 200 or "low" == (res_data["resourceSets"][0]["resources"][0]["confidence"]).lower():
            return None, None
        else:
            if "locality" in res_data["resourceSets"][0]["resources"][0]["address"]:
                return res_data["resourceSets"][0]["resources"][0]["address"]["locality"], \
                       res_data["resourceSets"][0]["resources"][0]["name"]
            else:
                return "that", res_data["resourceSets"][0]["resources"][0]["name"]


class Zomato:

    def __init__(self):
        self.api_key = "a7e3c34603ce43509e9f1a1c606c0bc2"  ## Update Zomato API key here
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
        logger.info(str(data))
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
        logger.info(str(cuisines))
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

        names_of_all_rest = []
        for rest in list_of_all_rest:
            names_of_all_rest.append(rest["restaurant"]["name"])
        logger.info(str(names_of_all_rest))
        return names_of_all_rest

    def get_all_restraunts_without_cuisne(self, location):
        '''
        Takes city name as arguments.
        Returns a list of 5 restaurants.
        '''
        logger.info("In without cuisine method")
        location_info = self.getZomatoLocationInfo(location)
        logger.info(str(location_info))
        queryString = {
            "entity_type": location_info[3],
            "entity_id": location_info[2],
            "count": 5
        }

        headers = {'Accept': 'application/json', 'user-key': self.api_key}
        res = requests.get(self.base_url + "search", params=queryString, headers=headers)
        logger.info(str(res))
        list_of_all_rest = res.json()["restaurants"]

        names_of_all_rest = []
        for rest in list_of_all_rest:
            names_of_all_rest.append(rest["restaurant"]["name"])
        logger.info(str(names_of_all_rest))
        return names_of_all_rest
