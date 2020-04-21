## Story_1
* telling_location_cuisine: i am looking to eat [chinese](cuisine) food in mumbai
    - slot{"cuisine":"chinese"}
    - action_show_restaurants
    - utter_ask_for_booking
* affirm: yes
    - restaurant_form
    - form{"name":"restaurant_form"}
    - slot{"requested_slot":"num_people"}
* telling_numpeople: book it for [5](phone_num[5](number)
    - restaurant_form
    - slot{"num_people":5}
    - slot{"requested_slot":"phone_num"}
* telling_phonenum: it is [8700981516]([8700981516](number)
    - restaurant_form
    - slot{"phone_num":8700981516}
    - slot{"requested_slot":"time"}
* telling_datetime: i will be visiting [2020-04-20T18:00:00.000+00:00](time)
    - restaurant_form
    - slot{"time":"2020-04-20T18:00:00.000+00:00"}
    - form{"name":null}
    - slot{"requested_slot":null}
    - utter_slot_values

Save end-to-end test



## Story_2
* greet: hi
    - utter_greet
* restaurant_search: ohk find me some restaurants then
    - utter_ask_location
* telling_location: yes it is hyderabad
    - action_set_location
    - slot{"location":"Hyderabad, India"}
    - utter_ask_cuisine
* telling_cuisine: [italian](cuisine) please
    - slot{"cuisine":"italian"}
    - slot{"cuisine":"italian"}
    - action_show_restaurants
    - utter_ask_for_booking
* affirm: yes
    - restaurant_form
    - form{"name":"restaurant_form"}
    - slot{"requested_slot":"num_people"}
    - slot{"cuisine":"italian"}
* telling_numpeople: yes it is [6](number) people
    - restaurant_form
    - slot{"num_people":6}
    - slot{"requested_slot":"phone_num"}
* telling_phonenum: it is [9711236651]([9711236651](number)
    - restaurant_form
    - slot{"phone_num":9711236651}
    - slot{"requested_slot":"time"}
* telling_datetime: i will be visiting [2020-04-21T20:00:00.000+00:00](time)
    - restaurant_form
    - slot{"time":"2020-04-21T20:00:00.000+00:00"}
    - form{"name":null}
    - slot{"requested_slot":null}
    - utter_slot_values

Save end-to-end test



## Story3
* greet: hey
    - utter_greet
* mood_great: i am good
    - utter_ask_location
* telling_location: yes i am living in hyderabad
    - action_set_location
    - slot{"location":"Hyderabad, India"}
    - utter_ask_cuisine
* telling_cuisine: i would like to eat [chinese](cuisine) food
    - slot{"cuisine":"chinese"}
    - slot{"cuisine":"chinese"}
    - action_show_restaurants
    - utter_ask_for_booking
* affirm: yes please
    - restaurant_form
    - form{"name":"restaurant_form"}
    - slot{"requested_slot":"num_people"}
* telling_numpeople: we are total [5](number) people
    - restaurant_form
    - slot{"num_people":5}
    - slot{"requested_slot":"phone_num"}
* telling_phonenum: ohk it is [8700981516]([8700981516](number)
    - restaurant_form
    - slot{"phone_num":8700981516}
    - slot{"requested_slot":"time"}
    - slot{"cuisine":"chinese"}
* telling_datetime: will be visiting [2020-04-22T00:00:00.000+00:00](time) at night
    - restaurant_form
    - slot{"time":"2020-04-22T00:00:00.000+00:00"}
    - form{"name":null}
    - slot{"requested_slot":null}
    - utter_slot_values
* affirm: thanks
    - utter_goodbye

Save end-to-end test


## New Story
* telling_location_cuisine: i want to eat [italian](cuisine) food in chennai
    - slot{"cuisine":"italian"}
    - action_show_restaurants
    - utter_ask_for_booking
* deny: no thanks
    - utter_goodbye
    
    
## New Story
* telling_location_cuisine: i want to eat [chinese](cuisine) food in punjab
    - slot{"cuisine":"chinese"}
    - slot{"cuisine":"chinese"}
    - action_show_restaurants
    - utter_ask_for_booking
    - slot{"cuisine":"chinese"}
* affirm: yes please
    - restaurant_form
    - form{"name":"restaurant_form"}
    - slot{"requested_slot":"num_people"}
* telling_numpeople: we are [3](num_people[3](number)
    - restaurant_form
    - slot{"num_people":3}
    - slot{"requested_slot":"phone_num"}
* telling_phonenum: its [7656543211]([7656543211](number)
    - restaurant_form
    - slot{"phone_num":7656543211}
    - slot{"requested_slot":"time"}
* telling_datetime: i will visit [2020-04-21T18:00:00.000+00:00](time)
    - restaurant_form
    - slot{"time":"2020-04-21T18:00:00.000+00:00"}
    - form{"name":null}
    - slot{"requested_slot":null}
    - utter_slot_values

Save end-to-end test



