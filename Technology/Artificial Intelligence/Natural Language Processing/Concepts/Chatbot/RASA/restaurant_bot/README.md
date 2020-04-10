## RestaurantBot

In this tutorial, **we will build a simple to complex restaurant bot step by step with the objective of exploring all awesome features of RASA** and make a personal assistant for yourself or for your business. 
We assume you have gone through the chatbot introduction,  various types of the chatbot, how to select chatbot as a project, It’s design practice, etc. 
If not then we highly recommend that you read the README of this section.

In this phase, we will be building a simple flow where users can search restaurants on bot through Zomato API based location and cuisine. 
As per the best design practice, the bot should welcome the user with the greeting and let the user know what bot can do. 
If user request matches with in-flow intents and if there are no or missing entities in the utterance then bot should ask required entities (cuisine and location in this phase) to complete the action (search restaurant from Zomato API). 
Here will train our model to extract cuisine and will use Bing map API to extract location as it’s impossible to train every damn location. 

To hit Zomato API with location we need entity_id, entity_type, lat and long which will get from [/location](https://developers.zomato.com/documentation#!/location/locations) and for cuisine, we need cuisine_id which you will get from [/cuisines](https://developers.zomato.com/documentation#!/common/cuisines)
Once we have all the details we can hit [/search](https://developers.zomato.com/documentation#!/restaurant/search) which is the main and final endpoint where you will get restaurant details. By default, you will get 20 top matched restaurants. We kept count as 5. Play around with Zomato API to get comfortable with it: https://developers.zomato.com/documentation

Look at the below self-explanatory state diagram which shows conversation flow with all required states.
<p align="center">
  <img width="460" height="300" src="conversation_flow.jpg" alt="Conversation diagram">
</p>

### What is Rasa?
[Rasa](https://rasa.com/docs/rasa/) is an open-source machine learning framework for building [contextual AI assistants and chatbots](https://blog.rasa.com/level-3-contextual-assistants-beyond-answering-simple-questions/).  
To make complete AI-based chatbot it has to handle two things: 

* Understanding the user’s message which is done through Rasa [NLU](https://rasa.com/docs/rasa/nlu/about/).
* The bot should be able to carry dialogue with context which is done by Rasa [Core](https://rasa.com/docs/rasa/core/about/).

Rasa’s document is very intuitive so in this tutorial, I will direct to appropriate section of the document.

### Skeleton of Rasa
Since hype was to match chatbot with humans. We will take the human analogy to understand the components of the chatbot. 

#### Bot configuration
Firstly we will understand the body parts of the human(mostly brain, Don’t worry it’s not biology class) which we call “Bot configuration” in the bot world. 

Primary thing we humans do is communicate. And language is the primary means of communication. So for the bot as well we need to set language. We will use the English language for the bot. But you can build a multi-lingual bot with RASA.  
For more information about languages supported by rasa refer: https://rasa.com/docs/rasa/nlu/language-support/

Now put on your apron and get ready with a scalpel to see what’s in the brain 😃. Seems like it’s way complex. Chuck it, but the point is whenever we hear something we process the information through millions of neurons to understand the meaning of the sentence with its context, etc. And our brain is smart enough to generate a proper response based on a question. So are we going to build that intelligent bot?. Hold on! We can but not right now. The best way to think and start building a chatbot is like a newborn baby. It learns with experience :) Now let’s understand how the brain of chatbot works. It’s called NLU(Natural language understanding) unit where it’s components do the job. Component includes as follows.

1. Tokenization: 
We read and understand the sentence word by word, right? Similarly, tokenizer will break the sentence into words(called word tokenizer).   
For more information on RASA supported tokenizer refer: https://rasa.com/docs/rasa/nlu/components/#tokenizers

2.  Featurizer: 
We infer meaning by words and when all words are combined in a sentence then we infer the meaning of the sentence with context, right? Similarly, tokenized words are used as features to the post components of the pipeline. These features are has meaning of the word(mathematically) which is called Embeddings. Get to know more about word embedding here. Embedding comes in below two flavors.   
    ###### Embedding:  
	1. Pre-trained:   
Here word embeddings are already trained on huge text datasets with various state-of-the-art architecture. Popular word embeddings are XLNet, BERT, Glove, etc. We can use word embedding as it is in our NLP pipeline when we don’t have much training data. This technique is called as transfer learning.  
	2. From scratch:   
When pre-trained does not work well because it might have trained on your domain-specific then we can train our own word embedding from scratch. It is recommended when you have sufficient training samples.   
RASA supports both types of word embedding. Refer this for more: https://rasa.com/docs/rasa/nlu/choosing-a-pipeline/#a-longer-answer  
For more information on RASA supported featurizers refer:  https://rasa.com/docs/rasa/nlu/components/#featurizers    
     3. Count vectorizer:  
       You can convert a sentence into features using a bag of words. Where you can have unigram, bi-gram, tri-gram.   
Check this for more information: https://rasa.com/docs/rasa/nlu/components/#countvectorsfeaturizer  
> Another interesting tweak is to increase the number of n-grams, which is 1 by default. By using a max_ngram of 2, you will create additional features for each couple of consecutive words. For example, if you want to recognize “I'm happy” and “I'm not happy” as different intents, it helps to have not happy as a feature.

3. Entity extraction   
These are a chunk of information we extract from sentences to complete the action. For example when we say `I want to travel from Hyderabad to Mumbai by flight`. Here the intent is “travel_flight" and to fetch information we need to know source i.e Hyderabad and destination i.e Mumbai and couple more entities like date of travel etc.

Once the intent is identified and all entity is extracted then we can complete the action by calling the required API.

Read more about entity extraction here: https://rasa.com/docs/rasa/nlu/entity-extraction/
 
4. Classifier  
Now you know the meaning(features) of the sentence(words through tokenization). It’s time to classify to its appropriate category. For e.g `I want to travel by cab` should classify to travel_cab and `I want to travel by flight` travel_flight. All this is done by using Machine learning or Deep learning classifier.  
Read more about supported RASA classifier here: https://rasa.com/docs/rasa/nlu/components/#intent-classifiers  
For more information about NLU pipeline and it’s component refer: https://rasa.com/docs/rasa/nlu/choosing-a-pipeline/ & https://rasa.com/docs/rasa/nlu/components/

Also read this in-depth information about NLU here: https://blog.rasa.com/rasa-nlu-in-depth-part-1-intent-classification/ 

Core policy
Till now we saw how chatbot understands the user sentence and classifies to proper intent and extract entities. 
But we humans follow natural conversation where we remember context and reply accordingly. Otherwise, it will look something like this. Frustrating 😠 isn't it?  
<p align="center">
  <img src="chatbot_human_chat.png" alt="chatbot_human_chat.png">
</p>

So how does rasa handles all this? It is done through various elements of the RASA. Let’s look at the architecture of the RASA.
<p align="center">
  <img width="460" height="300" src="rasa_architecture.png" alt="RASA Architecture">
</p>

Here Interpreter is part of NLU and Tracker, policy and action are part of Core.
* The message is passed to an Interpreter, which converts it into a dictionary including the original text, the intent, and any entities that were found.
* The Tracker is the object which keeps track of the conversation state. It receives the info that a new message has come in. Know more about it here: https://rasa.com/docs/rasa/api/tracker-stores/
* The policy receives the current state of the tracker, chooses the next action which is logged by the tracker and response is sent to the user. There are different policies to choose from.   
You will get more information here: https://rasa.com/docs/rasa/core/policies/#policies  
Along with policy “slots” which act as bot’s memory(context). It also influences how the dialogue progresses. Read more about slots here: https://rasa.com/docs/rasa/core/slots/

These settings are part of config.yml (Think this file as the brain of chatbot :P)

So far so good? We have gone through the psychology of the bot. Now it’s time to look at the environment of the chatbot which will help it to learn. 
Just like a growing baby, he/she learn from whatever is experienced. Similarly will need to train a chatbot with right training data.   
Which comes in the form of text utterances part of defined intent with the tagged entity for training NLU and as a story(like a conversation) to train RASA core.   
Read more about training data for NLU here: https://rasa.com/docs/rasa/nlu/training-data-format/ and for stories here: https://rasa.com/docs/rasa/core/stories/

As planned before we need to be very thorough with the scope of the bot. Hence we need to define its own universe in which our bot operates. It has the intents which it should classify to, entities which it should extract, slots which it should remember to maintain context, and actions which it should perform to complete the task. And response templates which bot should utter back. Read more about domain file here: https://rasa.com/docs/rasa/core/domains/
> Actions are the things your bot runs in response to user input.  
Read more about actions here: https://rasa.com/docs/rasa/core/actions/

Now we have all the ingredients ready to build a chatbot.
* Defining the scope of the bot ✅
* Exploring Zomato API ✅
* Understand RASA and its components ✅

## Now let’s set up and develop

#### Setup and installation instructions:
* Please follow the installation instruction mentioned here: [Installation instructions](installation-instructions.md)

Go through this quick RASA tutorial: https://rasa.com/docs/rasa/user-guide/rasa-tutorial/ for quick setup.

Now let’s add missing spices one by one to completely prepare the delicious dish.  
1. Understand the chatbot’s conversation flow again and create an NLU and story training data based on that.
  Few pointers: 
  * Assume that you are the first user who is talking to the bot and thinks of all-natural and quirky conversation you can have :P and prepare NLU and stories training data.
Don’t forget to include small talk(greetings, deny etc) in the training data.
Keep the all intents mutually exclusive and diversity in its utterance.
	> Note: No need to have comprehensive training data because we are going to explore rasa x to do the same in a much more comfortable way.

* Set appropriate NLU pipeline and policy configuration.
> For NLU we will use the English language and default spacy pipeline (pretrained_embeddings_spacy).
> For Core, we will use MemoizationPolicy and KerasPolicy. As it’s ML-based bot. Explore other ways to build the bot.
* Write a domain.yml file.
* Write an action.py file - action.py file is self-explanatory as all classes and functions are well commented.
* Write an endpoint.yml file - this file contains the different endpoints which your bot can connect to. Like tracker store, events, actions, etc.

Now it’s time to train the bot. 
Execute below command and explore this for more training options: https://rasa.com/docs/rasa/user-guide/command-line-interface/#train-a-model  
`rasa train`  

Let’s see how bot performs with limited training data and let’s explore rasa x and improve it.
Run the following command in every new tab.  
`rasa run actions`  
`rasa x`  

Open rasa x for testing and improving the story through interactive learning. Check [Juste's video intro to Rasa X](https://www.youtube.com/watch?v=VXvWdrr2yw8&feature=youtu.be) for more information.

In next phase will add more interesting features which include. 
   1. Deployment to FB along with Rich Media support.
   2. Will evaluate NLU and Stories with testing data
   3. Will make search query more complex by adding date time, distance, establishment etc
   4. Will add table booking options as well using Form policy in Core.
   5. Deployment to Heroku.
   6. _More features coming soon_

Please give a star to the repo and add your self to the watcher list so that you don't miss any of our updates.
Also, get added to our [FB community](https://www.facebook.com/groups/colearninglounge/).

#### Rasa learning resources
* [AI assistant building using Rasa - Co-learning lounge | YouTube](https://www.youtube.com/playlist?list=PLH0lCpFdVeJsivOaV1UJo-RxapzZ44-Cq)
* [Rasa master class | YouTube](https://www.youtube.com/watch?v=rlAQWbhwqLA&list=PL75e0qA87dlHQny7z43NduZHPo6qd-cRc)
* [Rasa docs | Official](https://rasa.com/docs/)

> **This tutorial is intended to be a public resource. As such, if you see any glaring inaccuracies or if a critical topic is missing, please feel free to point it out or (preferably) submit a pull request to improve the tutorial. Also, we are always looking to improve the scope of this article. For anything feel free to mail us @ colearninglounge@gmail.com**

> **Author of this article is Yogesh Kothiya. You can follow him on __[LinkedIn](https://www.linkedin.com/in/yogeshkothiya/)__, __[Medium](https://medium.com/@kothiya.yogesh)__, __[GitHub](https://github.com/kothiyayogesh)__, __[Twitter](https://twitter.com/Yogesh_Kothiya)__.**   
> Many thanks to [Vishal Pandey](https://www.linkedin.com/in/vishal-pandey-8243a2107/) and [Harin Joshi](https://www.linkedin.com/in/harin-joshi-44b812183/) for contributing in the project.

