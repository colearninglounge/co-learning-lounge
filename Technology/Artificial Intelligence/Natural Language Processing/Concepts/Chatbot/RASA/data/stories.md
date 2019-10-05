## say goodbye
* goodbye
  - utter_goodbye

## greet_restaurantSearch_tellingLocation_tellingCuisine

* greet
    - utter_greet
* mood_great
    - utter_assist
* restaurant_search
    - utter_ask_location
* telling_location
    - utter_affirm_location
    - action_set_location
    - slot{"location":"Hyderabad"}
    - utter_ask_cuisine
* telling_cuisine{"cuisine":"chinese"}
    - slot{"cuisine":"chinese"}
    - action_show_restaurants
* affirm
    - utter_goodbye
* goodbye

## greet_tellingLocationCuisine_bye

* greet
    - utter_greet
* mood_great
    - utter_assist
* telling_location_cuisine{"cuisine":"italian"}
    - slot{"cuisine":"italian"}
    - action_show_restaurants
* goodbye

## restaurantSearch_tellingLocation_tellingCuisine

* restaurant_search
    - utter_ask_location
* telling_location
    - action_set_location
    - slot{"location":"Mumbai"}
    - utter_affirm_location
    - utter_ask_cuisine
* telling_cuisine{"cuisine":"italian"}
    - slot{"cuisine":"italian"}
    - action_show_restaurants
* affirm
    - utter_goodbye

## tellingLocationCuisine

* telling_location_cuisine{"cuisine":"chinese"}
    - slot{"cuisine":"chinese"}
    - action_show_restaurants
* affirm
    - utter_goodbye

## greet_restaurantSearch_tellingLocation_denyLocation_tellingCuisine

* greet
    - utter_greet
* mood_great
    - utter_assist
* restaurant_search
    - utter_ask_location
* deny
    - utter_location_denied
* telling_location
    - action_set_location
    - slot{"location":"Hyderabad"}
    - utter_affirm_location
    - utter_ask_cuisine
* telling_cuisine{"cuisine":"chinese"}
    - slot{"cuisine":"chinese"}
    - action_show_restaurants
* affirm
    - utter_goodbye

## restaurantSearch_denyLocation_tellingLocation_tellingCuisine

* restaurant_search
    - utter_ask_location
* deny
    - utter_location_denied
* telling_location
    - action_set_location
    - slot{"location":"Mumbai"}
    - utter_affirm_location
    - utter_ask_cuisine
* telling_cuisine{"cuisine":"south indian"}
    - slot{"cuisine":"south indian"}
    - action_show_restaurants
* affirm
    - utter_goodbye

## greet_restaurantSearch_tellingLocation_denyCuisine_showRestaurantsWithoutCuisine

* greet
    - utter_greet
* mood_great
    - utter_assist
* restaurant_search
    - utter_ask_location
* telling_location
    - action_set_location
    - slot{"location":"Punjab"}
    - utter_affirm_location
    - utter_ask_cuisine
* deny
    - utter_itsok
    - action_restaurants_nocuisine
* affirm
    - utter_goodbye

## greet_restaurantSearch_denyLocation_denyLocation_bye

* greet
    - utter_greet
* mood_great
    - utter_assist
* restaurant_search
    - utter_ask_location
* deny
    - utter_location_denied
* deny
    - utter_tryAfter_sometime
    - utter_goodbye

## tellingLocation_tellingCuisine

* telling_location
    - action_set_location
    - slot{"location":"Mumbai"}
    - utter_affirm_location
    - utter_ask_cuisine
* telling_cuisine{"cuisine":"chinese"}
    - slot{"cuisine":"chinese"}
    - action_show_restaurants
* affirm
    - utter_goodbye

## tellingCuisine_tellingLocation_showRestaurants

* telling_cuisine{"cuisine":"italian"}
    - slot{"cuisine":"italian"}
    - utter_affirm_cuisine
    - utter_ask_location
* telling_location
    - action_set_location
    - slot{"location":"Hyderabad"}
    - action_show_restaurants
* affirm
    - utter_goodbye

## Chat with me

* greet
    - utter_greet
* telling_cuisine{"cuisine":"south indian"}
    - utter_affirm_cuisine
    - utter_ask_location
