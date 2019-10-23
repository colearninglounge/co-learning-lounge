//Firebase functions initialization and initialization
const functions = require('firebase-functions');
const firebaseAdmin = require('firebase-admin');
firebaseAdmin.initializeApp(functions.config().firebase);

//this will be required fro API calls
var req = require("request-promise");

//To debug dialogflow issues. When enabled developers can track longs and issues.
const { WebhookClient } = require('dialogflow-fulfillment');
process.env.DEBUG = 'dialogflow:debug'; // enables lib debugging statements

//Bing API
const bing_base_url = "https://dev.virtualearth.net/REST/v1/Locations";
const bing_api_key = "YOUR_BING_API_KEY";

//Zomato API
const zomato_base_url = "https://developers.zomato.com/api/v2.1/";
const zomato_api_key = "YOUR_ZOMATO_API_KEY";

exports.dialogflowFirebaseFulfillment = functions.https.onRequest((request, response) => {
    const agent = new WebhookClient({ request, response });
    console.log('Dialogflow Request headers: ' + JSON.stringify(request.headers));
    console.log('Dialogflow Request body: ' + JSON.stringify(request.body));

    function welcome(agent) {
        agent.add(`Hi there! Hope your day has been good so far! So what may I help you with today.`);
    }

    function fallback(agent) {
        agent.add(`Mmm.. I did not quite get that. ` +
            `But I can surly help your search restaurants once you provide me the right location and cuisine.`);
    }
    
    //Functions for API Calls
    async function get_bing_location_info(agent) {
        // console.log('Bring API Call');
        var userQuery = request.body.queryResult.queryText;

        var url = `${bing_base_url}?query=${userQuery}&key=${bing_api_key}`;
        return req(url).then(result => {
            var data = JSON.parse(result);
            // console.log(data["resourceSets"][0]["resources"][0]["point"]["coordinates"]);
            if(data["resourceSets"][0]["resources"].length === 0) {
                agent.add(`Could you please provide me the location details.`);
                return;
            }
            // data["resourceSets"][0]["resources"][0]["point"]["coordinates"]
            // console.log(data["resourceSets"][0]["resources"][0]["name"]);
            return data["resourceSets"][0]["resources"][0]["name"];
        })
        .catch(error =>{
            console.log('Error');
            console.log(error);
            agent.add(`I'm sorry! There seem to have been a glitch. Could you please try again in a bit. Thank You!`);
            return;
        });
    }
    
    async function get_location_info(bingApiResult, agent){
        // console.log('Location Info API Call');
        var options = { 
            method: 'GET',
            url: zomato_base_url+"locations",
            qs: {"query": bingApiResult},
            headers: { 
                'user-key': zomato_api_key,
                'content-type': 'application/json'
            },
        };
        return req(options).then(zomatoResult => {
            var response = JSON.parse(zomatoResult);
            // var city_id = response.location_suggestions[0].city_id;
            var location_info = [];
            location_info.push(response.location_suggestions[0].latitude);
            location_info.push(response.location_suggestions[0].longitude);
            location_info.push(response.location_suggestions[0].entity_id);
            location_info.push(response.location_suggestions[0].entity_type);

            // console.log(location_info);
            return location_info;
        })
        .catch(error =>{
            console.log('Error');
            console.log(error);
            agent.add(`I'm sorry! There seem to have been a glitch. Could you please try again in a bit. Thank You!`);
            return;
        });
    }

    async function get_cuisines(location_info, agent) {
        // console.log('Cuisines API Call');
        var options = { 
            method: 'GET',
            url: zomato_base_url+"cuisines",
            qs: {"lat": location_info[0], "lon": location_info[1]},
            headers: { 
                'user-key': zomato_api_key,
                'content-type': 'application/json'
            },
        };
        return req(options).then(zomatoResult => {
            var response = JSON.parse(zomatoResult);
            // console.log(response.cuisines);
            var all_cuisines_in_a_city = [];
            response.cuisines.forEach(x=>{
                all_cuisines_in_a_city.push([
                    x['cuisine'].cuisine_id,
                    x['cuisine'].cuisine_name
                ]);
            });

            // console.log(all_cuisines_in_a_city.length);
            // console.log(all_cuisines_in_a_city);
            return all_cuisines_in_a_city;
        })
        .catch(error =>{
            console.log('Error');
            console.log(error);
            agent.add(`I'm sorry! There seem to have been a glitch. Could you please try again in a bit. Thank You!`);
            return;
        });
    }

    async function get_five_restraunts(location_info, selected_cuisine_id, agent) {
        // console.log('Restaurent search API Call');
        var options = { 
            method: 'GET',
            url: zomato_base_url+"search",
            qs: { "entity_type": location_info[3], "entity_id": location_info[2], "cuisines": selected_cuisine_id, "count": 5},
            headers: { 
                'user-key': zomato_api_key,
                'content-type': 'application/json'
            },
        };
        return req(options).then(zomatoResult => {
            var response = JSON.parse(zomatoResult)["restaurants"];
            var restaurants = '';
            // console.log('restaurants API Demo');
            // console.log(response);
            if(response.length == 0) {
                agent.add(`Sorry! I did not find any restaurants near by with this cuisine.`);
            }

            if(response.length > 1) {
                for (i = 0; i < response.length - 1; i++) {
                restaurants += `${response[i].restaurant.name}, `;
                }
                restaurants += ` and ${response[response.length - 1].restaurant.name}`;
            } else {
                restaurants = `${response[response.length - 1].restaurant.name}`;
            }
            // console.log(restaurants);
            return restaurants;
        })
        .catch(error =>{
            console.log('Error');
            console.log(error);
            agent.add(`I'm sorry! There seem to have been a glitch. Could you please try again in a bit. Thank You!`);
            return;
        });
    }

    async function get_all_restraunts_without_cuisne(location_info, agent) {
        var options = { 
            method: 'GET',
            url: zomato_base_url+"search",
            qs: { "entity_type": location_info[3], "entity_id": location_info[2], "count": 5},
            headers: { 
                'user-key': zomato_api_key,
                'content-type': 'application/json'
            },
        };
        return req(options).then(zomatoResult => {
            var response = JSON.parse(zomatoResult)["restaurants"];
            var restaurants = '';
            if(response.length > 1) {
                for (i = 0; i < response.length - 1; i++) {
                restaurants += response[i].restaurant.name;
                }
                restaurants += ` and ${response[response.length - 1].restaurant.name}`;
            } else {
                restaurants = `${response[response.length - 1].restaurant.name}`;
            }
            return restaurants;
        })
        .catch(error =>{
            console.log('Error');
            console.log(error);
            agent.add(`I'm sorry! There seem to have been a glitch. Could you please try again in a bit. Thank You!`);
            return;
        });
    }
    //End of functions for API Calls

    
    //Start Intent handling functions
    async function locationCusine(agent) {
        
        var location_info = [];
        var all_cuisines_in_a_city = [];
        var selected_cuisine_id = '';

        var cuisine = agent.parameters['Cuisines'];

        var bingApiResult = await get_bing_location_info(agent);
        // console.log('After the bing API Call');
        // console.log(bingApiResult);

        //fetching city id using location
        var location_info = await get_location_info(bingApiResult, agent);
        // console.log('After the location API Call');
        // console.log(location_info);
        
        //fetching cuisines using location info
        var all_cuisines_in_a_city = await get_cuisines(location_info, agent);
        // console.log('After the cuisines api call');
        // console.log(all_cuisines_in_a_city.length);
        // console.log(all_cuisines_in_a_city[0]);

        for(var value in all_cuisines_in_a_city){
            if(all_cuisines_in_a_city[value][1].toLowerCase() === cuisine.toLowerCase()) {
                selected_cuisine_id = all_cuisines_in_a_city[value][0];
                console.log('Match found');
            }
        }
        console.log('After the comparision');
        console.log(selected_cuisine_id);

        //check if you found the cusine the user asked
        if(!selected_cuisine_id){
            response = `Hey! Seems like there aren't any near by restaurants who provide this cuisine. ` +
                `Please choose a different cuisine.`; 
        } else {
            var restaurants = await get_five_restraunts(location_info, selected_cuisine_id, agent);

            response = `Here is a list of a few restaurants that I found. Hope this helps. Have a great day! `;
            response += `${restaurants}`;
        }
        agent.add(response);
    }

    function restaurantSearch(agent) {
        agent.add('Sure. Could you please let me know the locations in which you want me to list the restaurants?');
    }
    
    async function tellingLocation(agent) { 
        var all_cuisines_in_a_city = [];       
        var location_info = [];
        var response = '';
        
        var bingApiResult = await get_bing_location_info(agent);

        //fetching city id using location
        location_info = await get_location_info(bingApiResult, agent);
        
        //fetching cuisines using location info
        all_cuisines_in_a_city = await get_cuisines(location_info, agent);

        const original = agent.getContext('cuisine_info');
        // console.log(original);
        if(original === null) {
            respose = `Which cuisine do you prefer?`;
            // response = `There are around ${all_cuisines_in_a_city.length} cuisines around this locations. ` +
            //     `I'll list a few you can either choose from them or let me know your preference and I'll check if ` +
                // `if any resaturents near by provide that. `;

            // var list_cuisines = ''; 
            // if(all_cuisines_in_a_city.length > 1) {
            //     for (i = 0; i < all_cuisines_in_a_city.length - 1 && i <= 6; i++) {
            //         list_cuisines += `${all_cuisines_in_a_city[i][1]}, `;
            //     }
            //     list_cuisines += ` and ${all_cuisines_in_a_city[all_cuisines_in_a_city.length - 1][1]}`;
            // } else {
            //     list_cuisines = `${all_cuisines_in_a_city[all_cuisines_in_a_city.length - 1][1]}`;
            // }
            // response += list_cuisines;

            response = 'Which cuisine do you prefer?';
            agent.setContext({
                name: 'loc_info',
                lifespan: 2,
                parameters: { 
                    lat: `${location_info[0]}`,
                    lon: `${location_info[1]}`, 
                    entity_id: `${location_info[2]}`, 
                    entity_type: `${location_info[3]}`,
                    location: `${bingApiResult}`
                }
            });
        } else {
            var selected_cuisine_id = '';

            var cuisine = original.parameters.cuisine;
            // console.log(cuisine);
            var all_cuisines_in_a_city = await get_cuisines(location_info, agent);

            for(var value in all_cuisines_in_a_city){
                if(all_cuisines_in_a_city[value][1].toLowerCase() === cuisine.toLowerCase()) {
                    selected_cuisine_id = all_cuisines_in_a_city[value][0];
                    // console.log('Match found');
                }
            }
            // console.log('After the comparision');
            // console.log(selected_cuisine_id);
    
            //check if you found the cusine the user asked
            if(!selected_cuisine_id){
                response = `Hey! Seems like there aren't any near by restaurants who provide this cuisine. ` +
                    `Please choose a different cuisine.`; 
            } else {
                var restaurants = await get_five_restraunts(location_info, selected_cuisine_id, agent);
                // console.log(restaurants);
                response = `Here is a list of a few restaurants that I found. Hope this helps. Have a great day! `;
                response += `Location: ${bingApiResult}\n`;
                response += `Cuisine: ${cuisine}\n`;
                response += `Restaurants:\n`;
                response += `${restaurants}`;
            }
        }
        agent.add(response);
    }

    async function tellingCuisine(agent) {
        var selected_cuisine_id = '', response = '';
        var cuisine = agent.parameters['Cuisines'];
        var location_info = [];
        
        const original = agent.getContext('loc_info');
        if(original === null) { 
            agent.add('Please provide the location in which you are searching for the restaurants.');
            agent.setContext({
                name: 'cuisine_info',
                lifespan: 2,
                parameters: { 
                    cuisine: `${cuisine}`
                }
            });
            return;
        }
        location_info.push(original.parameters.lat);
        location_info.push(original.parameters.lon);
        location_info.push(original.parameters.entity_id);
        location_info.push(original.parameters.entity_type);
        location_info.push(original.parameters.location);
        // console.log('Location Information');
        // console.log(location_info);

        var all_cuisines_in_a_city = await get_cuisines(location_info, agent);

        for(var value in all_cuisines_in_a_city){
            if(all_cuisines_in_a_city[value][1].toLowerCase() === cuisine.toLowerCase()) {
                selected_cuisine_id = all_cuisines_in_a_city[value][0];
                // console.log('Match found');
            }
        }
        // console.log('After the comparision');
        // console.log(selected_cuisine_id);

        //check if you found the cusine the user asked
        if(!selected_cuisine_id){
            response = `Hey! Seems like there aren't any near by restaurants who provide this cuisine. ` +
                `Please choose a different cuisine.`; 
        } else {
            var restaurants = await get_five_restraunts(location_info, selected_cuisine_id, agent);
            // console.log(restaurants);
            response = `Here is a list of a few restaurants that I found. Hope this helps. Have a great day! `;
            response += `Location: ${location_info[4]}\n`;
            response += `Cuisine: ${cuisine}\n`;
            response += `Restaurants:\n`;
            response += `${restaurants}`;
        }
        agent.add(response);
    }

    function exit(agent){
        agent.add('Leaving so soon :( No worries. Hope I was of help. Feel free to drop in again.');
    }
    //End Intent handling functions

    let intentMap = new Map();
    intentMap.set('Default Welcome Intent', welcome);
    intentMap.set('Default Fallback Intent', fallback);

    intentMap.set('telling_location_cuisine', locationCusine);

    intentMap.set('restaurant_search', restaurantSearch);
    intentMap.set('telling_location', tellingLocation);
    intentMap.set('telling_cuisine', tellingCuisine);
    
    intentMap.set('goodbye', exit);
    agent.handleRequest(intentMap);
});
