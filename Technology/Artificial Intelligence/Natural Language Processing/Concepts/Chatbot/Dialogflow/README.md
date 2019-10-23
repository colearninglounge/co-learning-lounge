
# Dialogflow Introduction

<div style="border-style: solid; border-color: black; text-align: center; background-color: lightgreen; padding: 5px;">

### What is Dialogflow?

Dialogflow is an NLP (Natural Language Processing) based Chatbot framework. It provides users the ability to design and develop chatbots with or without code, depending on the user case. Dialogflow comes with various features, like one click integration to multiple platforms and website, multi-language support, sentiment analysis and a few others.  

Dialogflow is powered by Google’s infrastructure and state of the art technologies like machine learning and Speech-to-Text capabilities. 

Additional Features:
1.	Automatic spelling correction while accepting and understanding user queries
2.	Creating a serverless chatbot service made easy
3.	Automated phone service made easier – helps transform the IVR service as a whole
4.	Built-in analytics 

### Supported Integrations

Google Actions, Facebook Messenger, Slack, Viber, Twitter, Twilio IP, Twilio (Text Messaging), Skype, Telegram, Kik, Line, Cisco Spark, Amazon Alexa and Microsoft Cortana.
Let’s understand the terminologies now

### Agent

An agent is a natural language module of Dialogflow that has been trained to understand the human language. 
This agent is used to design, and conversation flows based on your use cases and train it based on collected user data or a pre-existing dataset.  

### Intent

Every conversation we have with a person has an intent. For example, I purchase a coffee from Starbucks the intent here is ‘Purchasing a coffee’. We use intents in Dialogflow to map users query (user-expressions) to and intent to carry forward a conversation with the user.  

<img src="https://cloud.google.com/dialogflow/docs/images/intent-match-forecast.svg" alt="Agent extracting data from end-user expression requesting weather" style="width:90%; display:block; margin-left:auto; margin-right:auto;">

A basic intent contains the following:
* Training phrases: These are example phrases for what end-users might say. When an end-user expression resembles one of these phrases, Dialogflow matches the intent. You don't have to define every possible example, because Dialogflow's built-in machine learning expands on your list with other, similar phrases.
* Action: You can define an action for each intent. When an intent is matched, Dialogflow provides the action to your system, and you can use the action to trigger certain actions defined in your system.
* Parameters: When an intent is matched at runtime, Dialogflow provides the extracted values from the end-user expression as parameters. Each parameter has a type, called the entity type, which dictates exactly how the data is extracted. Unlike raw end-user input, parameters are structured data that can easily be used to perform some logic or generate responses.
* Responses: You define text, speech, or visual responses to return to the end-user. These may provide the end-user with answers, ask the end-user for more information, or terminate the conversation.
The following diagram shows the basic flow for intent matching and responding to the end-user:

<img src="https://cloud.google.com/dialogflow/docs/images/intent-match-respond-basic.svg" alt="Agent and intent handling an end-user expression" style="width:600px; display:block; margin-left:auto; margin-right:auto;">

### Entity

With the help of NLP Dialogflow can structure the user query and certain key values or rather data from the query can be extracted for understand what exactly the user is request. Entity is a parameter of a user query and Dialogflow provide quite a few system entities which make the development easier. Entities created by developers are known as developer defined entities. 

### Context

If you are asked to get a present for a friend, what would you do? Would you directly visit a gift shop and start browsing through the gifts? I don’t think so. No one’s too kind these days to by something for someone without knowing why. You need context to choose a gift. Is it their birthday/Wedding/anniversary? Without context a sentence has no meaning. Dialogflow is a context driven chatbot platform. It handles conversation flows based on context. 

The following diagram shows an example that uses context for a banking agent.

<img src="https://cloud.google.com/dialogflow/docs/images/contexts-overview.svg" alt="Diagram of user interacting with intents and context." style="width:60%; display:block; margin-left:auto; margin-right:auto;">

1.	The end-user asks for information about their checking account.
2.	Dialogflow matches this end-user expression to the CheckingInfo intent. This intent has a checking output context, so that context becomes active.
3.	The agent asks the end-user for the type of information they want about their checking account.
4.	The end-user responds with "my balance".
5.	Dialogflow matches this end-user expression to the CheckingBalance intent. This intent has a checking input context, which needs to be active to match this intent. A similar SavingsBalance intent may also exist for matching the same end-user expression when a savings context is active.
6.	After your system performs the necessary database queries, the agent responds with the checking account balance.

There is a lot more that Dialogflow offers but we will keep adding more as and when we.
Each concept will be explained in details moving forward. For now you can go ahead and read through the following resources we think will help you understand each concepts in detal.

### References

* [Dialogflow Basics](https://cloud.google.com/dialogflow/docs/basics)
