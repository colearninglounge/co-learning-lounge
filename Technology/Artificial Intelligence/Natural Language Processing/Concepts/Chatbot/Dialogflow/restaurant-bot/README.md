# Restaurant Bot

<div style="border-style: solid; border-color: black; text-align: center; background-color: lightgreen; padding: 5px;">

### Objective

In this tutorial, we will build a simple flow where users can search restaurants on the bot with the help of Zomato API. By the end of this tutorial you will be able to build a chatbot for yourself or for your business. Please go through the Dialogflow introduction before you begin with the tutorial better if you are new to the platform. 

### Bot Workflow

As per the best design practice, the bot should welcome the user with a greeting and let the user know what it can do. If the user request matches with the intents and the respective response is sent to the user. If the intent requires an entity and the user hasn’t sent it in the request, then the bot should ask the required entities (like cuisine and location in this case) to complete the action (like search restaurant from Zomato API). We will be training the agent to extract cuisine and will use the Bing maps API to extract location information as it’s a time-consuming task to create an entity that has all the location details of the entire world or even just one country for that matter.

<div style="text-align:center">
  <img width="460" height="300" src="/img/workflow.png" alt="Restaurant Bot Workflow">
</div>

* To get cuisines in a location we need cuisine_id which you will get from /cuisines endpoint. 
* To get restaurants from Zomato API we need location information like location id (entity_id), location type (entity_type), latitude and longitude which we will get from /location endpoint. 
* Once we have all the details we can hit /search endpoint which is the main and final endpoint where you will get all the restaurant details. By default, you will get 20 top matched restaurants. For this development we are going with Top 5 so that we don’t clutter the chat screen. 
* You can also play around with Zomato API to get comfortable with it. 

### [Step 1: Setup and Installation](installarion-instructions.md)
### [Step 2: Conversation Design in Dialogflow](dialogflow-instructions.md)
### [Step 3: Firebase Fulfilment](firebase-fulfillment-instructions.md)
### [Step 4: Web Integration](web-integration-instructions.md)