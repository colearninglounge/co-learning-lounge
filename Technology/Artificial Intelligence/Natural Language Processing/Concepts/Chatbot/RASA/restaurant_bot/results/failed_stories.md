## Story11
* greet: hey there
    - utter_greet
* restaurant_search: show me nearby restaurants
    - utter_ask_location
* telling_location: its goa
    - action_set_location
    - slot{"location": "Goa"}
    - utter_ask_cuisine
* telling_cuisine: [continental](cuisine) please
    - slot{"cuisine": "continental"}
    - slot{"cuisine": "continental"}
    - action_show_restaurants
    - utter_ask_for_booking
* affirm: yes
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"requested_slot": "num_people"}
* form: telling_numpeople: [4](num_people[4](number) people   <!-- predicted: telling_numpeople: [4](num_people)[4](number:4) people -->
    - form: restaurant_form
    - slot{"num_people": 4}
    - slot{"requested_slot": "phone_num"}
* form: telling_phonenum: [8874588645]([8874588645](number)   <!-- predicted: telling_phonenum: [8874588645](phone_num)[8874588645](number:8874588645) -->
    - form: restaurant_form
    - slot{"phone_num": 8874588645}
    - slot{"requested_slot": "time"}
* form: telling_datetime: [4](num_people[2020-05-04T20:00:00.000+00:00](time)   <!-- predicted: telling_numpeople: [4](num_people)[4](number:4) -->
    - form: restaurant_form
    - slot{"time": "2020-05-04T20:00:00.000+00:00"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_slot_values
* goodbye: thankyou
    - utter_goodbye


## Story12
* telling_cuisine: i want to eat [mithai](cuisine)
    - slot{"cuisine": "mithai"}
    - slot{"cuisine": "mithai"}
    - utter_affirm_cuisine
    - utter_ask_location
* telling_location: jaipur
    - action_set_location
    - slot{"location": "Jaipur, India"}
    - action_show_restaurants
    - utter_ask_for_booking
* affirm: yes please
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"requested_slot": "num_people"}
* form: telling_numpeople: [2](num_people[2](number) people   <!-- predicted: telling_numpeople: [2](num_people)[2](number:2) people -->
    - form: restaurant_form
    - slot{"num_people": 2}
    - slot{"requested_slot": "phone_num"}
* form: telling_phonenum: [8826788729]([8826788729](number)   <!-- predicted: telling_phonenum: [8826788729](phone_num)[8826788729](number:8826788729) -->
    - form: restaurant_form
    - slot{"phone_num": 8826788729}
    - slot{"requested_slot": "time"}
* form: telling_datetime: [2020-04-28T00:00:00.000+00:00](time)   <!-- predicted: telling_datetime: [2020-04-28](time:2020-04-28T00:00:00.000+00:00)T[00:00:00.000](time:{'to': '2020-04-29T00:01:00.000+00:00', 'from': '2020-04-29T00:00:00.000+00:00'})+[00:00](time:2020-04-29T00:00:00.000+00:00) -->
    - form: restaurant_form
    - slot{"time": "2020-04-28T00:00:00.000+00:00"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_slot_values


## Story13
* telling_cuisine: i want to eat [north indian](cuisine)
    - slot{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_affirm_cuisine
    - utter_ask_location
* telling_location: jaipur
    - action_set_location
    - slot{"location": "Jaipur, India"}
    - action_show_restaurants
    - utter_ask_for_booking
* affirm: yes please
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"requested_slot": "num_people"}
* form: telling_numpeople: [3](num_people[3](number) people   <!-- predicted: telling_numpeople: [3](num_people)[3](number:3) people -->
    - form: restaurant_form
    - slot{"num_people": 3}
    - slot{"requested_slot": "phone_num"}
* form: telling_phonenum: [8826788729]([8826788729](number)   <!-- predicted: telling_phonenum: [8826788729](phone_num)[8826788729](number:8826788729) -->
    - form: restaurant_form
    - slot{"phone_num": 8826788729}
    - slot{"requested_slot": "time"}
* form: telling_datetime: [2020-04-28T00:00:00.000+00:00](time)   <!-- predicted: telling_datetime: [2020-04-28](time:2020-04-28T00:00:00.000+00:00)T[00:00:00.000](time:{'to': '2020-04-29T00:01:00.000+00:00', 'from': '2020-04-29T00:00:00.000+00:00'})+[00:00](time:2020-04-29T00:00:00.000+00:00) -->
    - form: restaurant_form
    - slot{"time": "2020-04-28T00:00:00.000+00:00"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_slot_values


## Story14
* telling_cuisine: i want to eat [south indian](cuisine)
    - slot{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_affirm_cuisine
    - utter_ask_location
* telling_location: kolkata
    - action_set_location
    - slot{"location": "Kolkata, India"}
    - action_show_restaurants
    - utter_ask_for_booking
* affirm: yes please
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"requested_slot": "num_people"}
* form: telling_numpeople: [4](num_people[4](number) people   <!-- predicted: telling_numpeople: [4](num_people)[4](number:4) people -->
    - form: restaurant_form
    - slot{"num_people": 4}
    - slot{"requested_slot": "phone_num"}
* form: telling_phonenum: [8826788729]([8826788729](number)   <!-- predicted: telling_phonenum: [8826788729](phone_num)[8826788729](number:8826788729) -->
    - form: restaurant_form
    - slot{"phone_num": 8826788729}
    - slot{"requested_slot": "time"}
* form: telling_datetime: [2020-04-28T00:00:00.000+00:00](time)   <!-- predicted: telling_datetime: [2020-04-28](time:2020-04-28T00:00:00.000+00:00)T[00:00:00.000](time:{'to': '2020-04-29T00:01:00.000+00:00', 'from': '2020-04-29T00:00:00.000+00:00'})+[00:00](time:2020-04-29T00:00:00.000+00:00) -->
    - form: restaurant_form
    - slot{"time": "2020-04-28T00:00:00.000+00:00"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_slot_values


## Story1
* telling_location_cuisine: i am looking to eat [chinese](cuisine) food in mumbai
    - slot{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_show_restaurants
    - utter_ask_for_booking
* affirm: yes
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"requested_slot": "num_people"}
* form: telling_numpeople: book it for [5](num_people[5](number) people   <!-- predicted: telling_numpeople: book it for [5](num_people)[5](number:5) people -->
    - form: restaurant_form
    - slot{"num_people": 5}
    - slot{"requested_slot": "phone_num"}
* form: telling_phonenum: it is [7756477890]([7756477890](number)   <!-- predicted: telling_phonenum: it is [7756477890](phone_num)[7756477890](number:7756477890) -->
    - form: restaurant_form
    - slot{"phone_num": 7756477890}
    - slot{"requested_slot": "time"}
* form: telling_datetime: i will be visiting [2020-04-27T19:00:00.000+00:00](time)   <!-- predicted: telling_datetime: i will be visiting [2020-04-27](time:2020-04-27T00:00:00.000+00:00)T[19:00:00.000](time:{'to': '2020-04-29T00:01:00.000+00:00', 'from': '2020-04-28T19:00:00.000+00:00'})+[00:00](time:2020-04-29T00:00:00.000+00:00) -->
    - form: restaurant_form
    - slot{"time": "2020-04-27T19:00:00.000+00:00"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_slot_values


## Story3
* greet: hi
    - utter_greet
* restaurant_search: ohk find me some restaurants then
    - utter_ask_location
* telling_location: yes it is hyderabad
    - action_set_location
    - slot{"location": "Hyderabad, India"}
    - utter_ask_cuisine
* telling_cuisine: [italian](cuisine) please
    - slot{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - action_show_restaurants
    - utter_ask_for_booking
* affirm: yes
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"requested_slot": "num_people"}
    - slot{"cuisine": "italian"}
* form: telling_numpeople: yes it is [6](num_people[6](number) people   <!-- predicted: telling_numpeople: yes it is [6](num_people)[6](number:6) people -->
    - form: restaurant_form
    - slot{"num_people": 6}
    - slot{"requested_slot": "phone_num"}
* form: telling_phonenum: it is [9711236651]([9711236651](number)   <!-- predicted: telling_phonenum: it is [9711236651](phone_num)[9711236651](number:9711236651) -->
    - form: restaurant_form
    - slot{"phone_num": 9711236651}
    - slot{"requested_slot": "time"}
* form: telling_datetime: i will be visiting [2020-04-21T20:00:00.000+00:00](time)   <!-- predicted: telling_datetime: i will be visiting [2020-04-21](time:2020-04-21T00:00:00.000+00:00)T[20:00:00.000](time:{'to': '2020-04-29T00:01:00.000+00:00', 'from': '2020-04-28T20:00:00.000+00:00'})+[00:00](time:2020-04-29T00:00:00.000+00:00) -->
    - form: restaurant_form
    - slot{"time": "2020-04-21T20:00:00.000+00:00"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_slot_values


## Story4
* greet: hey
    - utter_greet
* mood_great: i am good
    - utter_ask_location
* telling_location: yes i am living in hyderabad
    - action_set_location
    - slot{"location": "Hyderabad, India"}
    - utter_ask_cuisine
* telling_cuisine: i would like to eat [chinese](cuisine) food
    - slot{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_show_restaurants
    - utter_ask_for_booking
* affirm: yes please
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"requested_slot": "num_people"}
* form: telling_numpeople: we are total [5](num_people[5](number) people   <!-- predicted: telling_numpeople: we are total [5](num_people)[5](number:5) people -->
    - form: restaurant_form
    - slot{"num_people": 5}
    - slot{"requested_slot": "phone_num"}
* form: telling_phonenum: ohk it is [8700981516]([8700981516](number)   <!-- predicted: telling_phonenum: ohk it is [8700981516](phone_num)[8700981516](number:8700981516) -->
    - form: restaurant_form
    - slot{"phone_num": 8700981516}
    - slot{"requested_slot": "time"}
    - slot{"cuisine": "chinese"}
* form: telling_datetime: will be visiting [2020-04-22T00:00:00.000+00:00](time) at night   <!-- predicted: telling_datetime: will be visiting [2020-04-22](time:2020-04-22T00:00:00.000+00:00)T[00:00:00.000](time:{'to': '2020-04-29T00:01:00.000+00:00', 'from': '2020-04-29T00:00:00.000+00:00'})+[00:00](time:2020-04-29T00:00:00.000+00:00) at night -->
    - form: restaurant_form
    - slot{"time": "2020-04-22T00:00:00.000+00:00"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_slot_values
* affirm: thanks
    - utter_goodbye   <!-- predicted: action_default_fallback -->


## Story6
* telling_location_cuisine: i want to eat [chinese](cuisine) food in punjab
    - slot{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_show_restaurants
    - utter_ask_for_booking
* affirm: yes
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"requested_slot": "num_people"}
* form: telling_numpeople: we are [3](num_people[3](number)   <!-- predicted: telling_numpeople: we are [3](num_people)[3](number:3) -->
    - form: restaurant_form
    - slot{"num_people": 3}
    - slot{"requested_slot": "phone_num"}
* form: telling_phonenum: its [7765477654]([7765477654](number)   <!-- predicted: telling_phonenum: its [7765477654](phone_num)[7765477654](number:7765477654) -->
    - form: restaurant_form
    - slot{"phone_num": 7765477654}
    - slot{"requested_slot": "time"}
* form: telling_datetime: i will visit [2020-04-29T19:00:00.000+00:00](time)   <!-- predicted: telling_datetime: i will visit [2020-04-29](time:2020-04-29T00:00:00.000+00:00)T[19:00:00.000](time:{'to': '2020-04-29T00:01:00.000+00:00', 'from': '2020-04-28T19:00:00.000+00:00'})+[00:00](time:2020-04-29T00:00:00.000+00:00) -->
    - form: restaurant_form
    - slot{"time": "2020-04-29T19:00:00.000+00:00"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_slot_values
* goodbye: bye
    - utter_goodbye


## Story8
* restaurant_search: i am looking for [burger](cuisine)
    - slot{"cuisine": "burger"}
    - slot{"cuisine": "burger"}
    - action_default_fallback
* telling_cuisine: i want to eat [burger](cuisine)
    - slot{"cuisine": "burger"}
    - slot{"cuisine": "burger"}
    - utter_affirm_cuisine   <!-- predicted: action_show_restaurants -->
    - utter_ask_location   <!-- predicted: action_default_fallback -->
* telling_location: its chandni chowk
    - action_set_location
    - slot{"location": "Chandni Chowk, Chowringhee North, Kolkata 700072, India"}
    - action_show_restaurants
    - utter_ask_for_booking
* affirm: yes please
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"requested_slot": "num_people"}
* form: telling_numpeople: there will me [7](num_people[7](number) people   <!-- predicted: telling_numpeople: there will me [7](num_people)[7](number:7) people -->
    - form: restaurant_form
    - slot{"num_people": 7}
    - slot{"requested_slot": "phone_num"}
* form: telling_phonenum: [8898899900]([8898899900](number)   <!-- predicted: telling_phonenum: [8898899900](phone_num)[8898899900](number:8898899900) -->
    - form: restaurant_form
    - slot{"phone_num": 8898899900}
    - slot{"requested_slot": "time"}
* form: telling_datetime: [2020-04-28T16:00:00.000+00:00](time)   <!-- predicted: telling_datetime: [2020-04-28](time:2020-04-28T00:00:00.000+00:00)T[16:00:00.000](time:{'to': '2020-04-29T00:01:00.000+00:00', 'from': '2020-04-28T16:00:00.000+00:00'})+[00:00](time:2020-04-29T00:00:00.000+00:00) -->
    - form: restaurant_form
    - slot{"time": "2020-04-28T16:00:00.000+00:00"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_slot_values
* goodbye: thankyou
    - utter_goodbye


## Story9
* greet: hello there
    - utter_greet
* restaurant_search: i want to know about nearby restaurants
    - utter_ask_location
* telling_location: i am near pune
    - action_set_location
    - slot{"location": "Pune, India"}
    - utter_ask_cuisine
* telling_cuisine: [italian](cuisine)
    - slot{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - action_show_restaurants
    - utter_ask_for_booking
* affirm: yes please
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"requested_slot": "num_people"}
* form: telling_numpeople: there will be [20](num_peopl[20](number) people   <!-- predicted: telling_numpeople: there will be [20](num_people)[20](number:20) people -->
    - form: restaurant_form
    - slot{"num_people": 20}
    - slot{"requested_slot": "phone_num"}
* form: telling_phonenum: its [2345533242]([2345533242](number)   <!-- predicted: telling_phonenum: its [2345533242](phone_num)[2345533242](number:2345533242) -->
    - form: restaurant_form
    - slot{"phone_num": 2345533242}
    - slot{"requested_slot": "time"}
* form: telling_datetime: [2020-05-03T19:00:00.000+00:00](time)   <!-- predicted: telling_datetime: [2020-05-03](time:2020-05-03T00:00:00.000+00:00)T[19:00:00.000](time:{'to': '2020-04-29T00:01:00.000+00:00', 'from': '2020-04-28T19:00:00.000+00:00'})+[00:00](time:2020-04-29T00:00:00.000+00:00) -->
    - form: restaurant_form
    - slot{"time": "2020-05-03T19:00:00.000+00:00"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_slot_values
* goodbye: thankyou
    - utter_goodbye


