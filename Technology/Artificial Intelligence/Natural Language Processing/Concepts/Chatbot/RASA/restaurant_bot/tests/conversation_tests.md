## Story1
* telling_location_cuisine: i am looking to eat [chinese](cuisine) food in mumbai
    - slot{"cuisine":"chinese"}
    - action_show_restaurants
    - utter_ask_for_booking
* affirm: yes
    - restaurant_form
    - form{"name":"restaurant_form"}``
    - slot{"requested_slot":"num_people"}
* telling_numpeople: book it for [5](num_people[5](number) people
    - restaurant_form
    - slot{"num_people":5}
    - slot{"requested_slot":"phone_num"}
* telling_phonenum: it is [7756477890]([7756477890](number)
    - restaurant_form
    - slot{"phone_num":7756477890}
    - slot{"requested_slot":"time"}
* telling_datetime: i will be visiting [2020-04-27T19:00:00.000+00:00](time)
    - restaurant_form
    - slot{"time":"2020-04-27T19:00:00.000+00:00"}
    - form{"name":null}
    - slot{"requested_slot":null}
    - action_get_date_time
    - slot{"date_slot":"27/04/2020"}
    - slot{"time_slot":"19:00"}
    - utter_slot_values




## Story2
* greet: hey there
    - utter_greet
* restaurant_search: i am feeling hungry
    - utter_ask_location
* telling_location: i am near mohali
    - action_set_location
    - slot{"location":"Mohali, India"}
    - utter_ask_cuisine
* telling_cuisine: i want to eat [south indian](cuisine)
    - slot{"cuisine":"south indian"}
    - action_show_restaurants
    - utter_ask_for_booking
* deny: no
    - utter_goodbye


## Story3
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
    - action_show_restaurants
    - utter_ask_for_booking
* affirm: yes
    - restaurant_form
    - form{"name":"restaurant_form"}
    - slot{"requested_slot":"num_people"}
    - slot{"cuisine":"italian"}
* telling_numpeople: yes it is [6](num_people[6](number) people
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
    - action_get_date_time
    - slot{"date_slot":"21/04/2020"}
    - slot{"time_slot":"20:00"}
    - utter_slot_values





## Story4
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
    - action_show_restaurants
    - utter_ask_for_booking
* affirm: yes please
    - restaurant_form
    - form{"name":"restaurant_form"}
    - slot{"requested_slot":"num_people"}
* telling_numpeople: we are total [5](num_people[5](number) people
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
    - action_get_date_time
    - slot{"date_slot":"22/04/2020"}
    - slot{"time_slot":"00:00"}
    - utter_slot_values
* affirm: thanks
    - utter_goodbye



## Story5
* telling_location_cuisine: i want to eat [italian](cuisine) food in chennai
    - slot{"cuisine":"italian"}
    - action_show_restaurants
    - utter_ask_for_booking
* deny: no thanks
    - utter_goodbye
    
    
## Story6
* telling_location_cuisine: i want to eat [chinese](cuisine) food in punjab
    - slot{"cuisine":"chinese"}
    - action_show_restaurants
    - utter_ask_for_booking
* affirm: yes
    - restaurant_form
    - form{"name":"restaurant_form"}
    - slot{"requested_slot":"num_people"}
* telling_numpeople: we are [3](num_people[3](number)
    - restaurant_form
    - slot{"num_people":3}
    - slot{"requested_slot":"phone_num"}
* telling_phonenum: its [7765477654]([7765477654](number)
    - restaurant_form
    - slot{"phone_num":7765477654}
    - slot{"requested_slot":"time"}
* telling_datetime: i will visit [2020-04-29T19:00:00.000+00:00](time)
    - restaurant_form
    - slot{"time":"2020-04-29T19:00:00.000+00:00"}
    - form{"name":null}
    - slot{"requested_slot":null}
    - action_get_date_time
    - slot{"date_slot":"29/04/2020"}
    - slot{"time_slot":"19:00"}
    - utter_slot_values
* goodbye: bye
    - utter_goodbye



## Story7
* telling_cuisine: i want to eat [pizza](cuisine)
    - slot{"cuisine":"pizza"}
    - utter_affirm_cuisine
    - utter_ask_location
* telling_location: its Delhi
    - action_set_location
    - slot{"location":"Delhi"}
    - action_show_restaurants
    - utter_ask_for_booking
* deny: no
    - utter_goodbye


## Story8
* restaurant_search: i am looking for [burger](cuisine)
    - slot{"cuisine":"burger"}
    - action_default_fallback
* telling_cuisine: i want to eat [burger](cuisine)
    - slot{"cuisine":"burger"}
    - utter_affirm_cuisine
    - utter_ask_location
* telling_location: its chandni chowk
    - action_set_location
    - slot{"location":"Chandni Chowk, Chowringhee North, Kolkata 700072, India"}
    - action_show_restaurants
    - utter_ask_for_booking
* affirm: yes please
    - restaurant_form
    - form{"name":"restaurant_form"}
    - slot{"requested_slot":"num_people"}
* telling_numpeople: there will me [7](num_people[7](number) people
    - restaurant_form
    - slot{"num_people":7}
    - slot{"requested_slot":"phone_num"}
* telling_phonenum: [8898899900]([8898899900](number)
    - restaurant_form
    - slot{"phone_num":8898899900}
    - slot{"requested_slot":"time"}
* telling_datetime: [2020-04-28T16:00:00.000+00:00](time)
    - restaurant_form
    - slot{"time":"2020-04-28T16:00:00.000+00:00"}
    - form{"name":null}
    - slot{"requested_slot":null}
    - action_get_date_time
    - slot{"date_slot":"28/04/2020"}
    - slot{"time_slot":"16:00"}
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
    - slot{"location":"Pune, India"}
    - utter_ask_cuisine
* telling_cuisine: [italian](cuisine)
    - slot{"cuisine":"italian"}
    - action_show_restaurants
    - utter_ask_for_booking
* affirm: yes please
    - restaurant_form
    - form{"name":"restaurant_form"}
    - slot{"requested_slot":"num_people"}
* telling_numpeople: there will be [20](num_peopl[20](number) people
    - restaurant_form
    - slot{"num_people":20}
    - slot{"requested_slot":"phone_num"}
* telling_phonenum: its [2345533242]([2345533242](number)
    - restaurant_form
    - slot{"phone_num":2345533242}
    - slot{"requested_slot":"time"}
* telling_datetime: [2020-05-03T19:00:00.000+00:00](time)
    - restaurant_form
    - slot{"time":"2020-05-03T19:00:00.000+00:00"}
    - form{"name":null}
    - slot{"requested_slot":null}
    - action_get_date_time
    - slot{"date_slot":"03/05/2020"}
    - slot{"time_slot":"19:00"}
    - utter_slot_values
* goodbye: thankyou
    - utter_goodbye



## Story10
* telling_location_cuisine: [momos](cuisine) in hyderabad
    - slot{"cuisine":"momos"}
    - action_show_restaurants
    - utter_ask_for_booking
* deny: no
    - utter_goodbye



## Story11
* greet: hey there
    - utter_greet
* restaurant_search: show me nearby restaurants
    - utter_ask_location
* telling_location: its goa
    - action_set_location
    - slot{"location":"Goa"}
    - utter_ask_cuisine
* telling_cuisine: [continental](cuisine) please
    - slot{"cuisine":"continental"}
    - action_show_restaurants
    - utter_ask_for_booking
* affirm: yes
    - restaurant_form
    - form{"name":"restaurant_form"}
    - slot{"requested_slot":"num_people"}
* telling_numpeople: [4](num_people[4](number) people
    - restaurant_form
    - slot{"num_people":4}
    - slot{"requested_slot":"phone_num"}
* telling_phonenum: [8874588645]([8874588645](number)
    - restaurant_form
    - slot{"phone_num":8874588645}
    - slot{"requested_slot":"time"}
* telling_datetime: [4](num_people[2020-05-04T20:00:00.000+00:00](time)
    - restaurant_form
    - slot{"time":"2020-05-04T20:00:00.000+00:00"}
    - form{"name":null}
    - slot{"requested_slot":null}
    - action_get_date_time
    - slot{"date_slot":"04/05/2020"}
    - slot{"time_slot":"20:00"}
    - utter_slot_values
* goodbye: thankyou
    - utter_goodbye



## Story12
* telling_cuisine: i want to eat [mithai](cuisine)
    - slot{"cuisine":"mithai"}
    - utter_affirm_cuisine
    - utter_ask_location
* telling_location: jaipur
    - action_set_location
    - slot{"location":"Jaipur, India"}
    - action_show_restaurants
    - utter_ask_for_booking
* affirm: yes please
    - restaurant_form
    - form{"name":"restaurant_form"}
    - slot{"requested_slot":"num_people"}
* telling_numpeople: [2](num_people[2](number) people
    - restaurant_form
    - slot{"num_people":2}
    - slot{"requested_slot":"phone_num"}
* telling_phonenum: [8826788729]([8826788729](number)
    - restaurant_form
    - slot{"phone_num":8826788729}
    - slot{"requested_slot":"time"}
* telling_datetime: [2020-04-28T00:00:00.000+00:00](time)
    - restaurant_form
    - slot{"time":"2020-04-28T00:00:00.000+00:00"}
    - form{"name":null}
    - slot{"requested_slot":null}
    - action_get_date_time
    - slot{"date_slot":"28/04/2020"}
    - slot{"time_slot":"00:00"}
    - utter_slot_values



## Story13
* telling_cuisine: i want to eat [north indian](cuisine)
    - slot{"cuisine":"north indian"}
    - utter_affirm_cuisine
    - utter_ask_location
* telling_location: jaipur
    - action_set_location
    - slot{"location":"Jaipur, India"}
    - action_show_restaurants
    - utter_ask_for_booking
* affirm: yes please
    - restaurant_form
    - form{"name":"restaurant_form"}
    - slot{"requested_slot":"num_people"}
* telling_numpeople: [3](num_people[3](number) people
    - restaurant_form
    - slot{"num_people":3}
    - slot{"requested_slot":"phone_num"}
* telling_phonenum: [8826788729]([8826788729](number)
    - restaurant_form
    - slot{"phone_num":8826788729}
    - slot{"requested_slot":"time"}
* telling_datetime: [2020-04-28T00:00:00.000+00:00](time)
    - restaurant_form
    - slot{"time":"2020-04-28T00:00:00.000+00:00"}
    - form{"name":null}
    - slot{"requested_slot":null}
    - action_get_date_time
    - slot{"date_slot":"28/04/2020"}
    - slot{"time_slot":"00:00"}
    - utter_slot_values



## Story14
* telling_cuisine: i want to eat [south indian](cuisine)
    - slot{"cuisine":"south indian"}
    - utter_affirm_cuisine
    - utter_ask_location
* telling_location: kolkata
    - action_set_location
    - slot{"location":"Kolkata, India"}
    - action_show_restaurants
    - utter_ask_for_booking
* affirm: yes please
    - restaurant_form
    - form{"name":"restaurant_form"}
    - slot{"requested_slot":"num_people"}
* telling_numpeople: [4](num_people[4](number) people
    - restaurant_form
    - slot{"num_people":4}
    - slot{"requested_slot":"phone_num"}
* telling_phonenum: [8826788729]([8826788729](number)
    - restaurant_form
    - slot{"phone_num":8826788729}
    - slot{"requested_slot":"time"}
* telling_datetime: [2020-04-28T00:00:00.000+00:00](time)
    - restaurant_form
    - slot{"time":"2020-04-28T00:00:00.000+00:00"}
    - form{"name":null}
    - slot{"requested_slot":null}
    - action_get_date_time
    - slot{"date_slot":"28/04/2020"}
    - slot{"time_slot":"00:00"}
    - utter_slot_values



## Story15
* telling_cuisine: want to have [paan](cuisine)
    - slot{"cuisine":"paan"}
    - utter_affirm_cuisine
    - utter_ask_location
* telling_location: mumbai
    - action_set_location
    - slot{"location":"Mumbai, India"}
    - action_show_restaurants
    - utter_ask_for_booking
* deny: no
    - utter_goodbye



## Story16
* telling_location: i am near mumbai
    - action_set_location
    - slot{"location":"Mumbai, India"}
    - utter_ask_cuisine
* telling_cuisine: [african](cuisine)
    - slot{"cuisine":"african"}
    - action_show_restaurants
    - utter_ask_for_booking
* affirm: yes
    - restaurant_form
    - form{"name":"restaurant_form"}
    - slot{"requested_slot":"num_people"}
* telling_numpeople: [4](num_people[4](number) people
    - restaurant_form
    - slot{"num_people":4}
    - slot{"requested_slot":"phone_num"}
* telling_phonenum: its [8759899301]([8759899301](number)
    - restaurant_form
    - slot{"phone_num":8759899301}
    - slot{"requested_slot":"time"}
* telling_datetime: [2020-05-03T16:00:00.000+00:00](time)
    - restaurant_form
    - slot{"time":"2020-05-03T16:00:00.000+00:00"}
    - form{"name":null}
    - slot{"requested_slot":null}
    - action_get_date_time
    - slot{"date_slot":"03/05/2020"}
    - slot{"time_slot":"16:00"}
    - utter_slot_values
    
    
## Story17
* greet: hello
    - utter_greet
* mood_great: i am great
    - utter_ask_location
* telling_location: its chennai
    - action_set_location
    - slot{"location":"Chennai, India"}
    - utter_ask_cuisine
* telling_cuisine: [north indian](cuisine)
    - slot{"cuisine":"north indian"}
    - action_show_restaurants
    - utter_ask_for_booking
* affirm: yes please
    - restaurant_form
    - form{"name":"restaurant_form"}
    - slot{"requested_slot":"num_people"}
* telling_numpeople: [3](num_people[3](number) people
    - restaurant_form
    - slot{"num_people":3}
    - slot{"requested_slot":"phone_num"}
* telling_phonenum: [8877665544]([8877665544](number)
    - restaurant_form
    - slot{"phone_num":8877665544}
    - slot{"requested_slot":"time"}
* telling_datetime: [2020-05-03T21:00:00.000+00:00](time)
    - restaurant_form
    - slot{"time":"2020-05-03T21:00:00.000+00:00"}
    - form{"name":null}
    - slot{"requested_slot":null}
    - action_get_date_time
    - slot{"date_slot":"03/05/2020"}
    - slot{"time_slot":"21:00"}
    - utter_slot_values


    

## Story18
* greet: hey
    - utter_greet
* mood_great: i am fine
    - utter_ask_location
* deny: not sure
    - utter_location_denied


## Story19
* telling_cuisine: i want to eat some [mexican](cuisine) food
    - slot{"cuisine":"mexican"}
    - utter_affirm_cuisine
    - utter_ask_location
* telling_location: yeah its udaipur
    - action_set_location
    - slot{"location":"Udaipur, India"}
    - action_show_restaurants
    - utter_ask_for_booking
* deny: no
    - utter_goodbye
    