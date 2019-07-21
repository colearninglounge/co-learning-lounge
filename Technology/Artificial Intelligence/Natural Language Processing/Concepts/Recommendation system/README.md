## Recommendation system
Recommender systems are pretty self-explanatory; as the name suggests, they are systems or techniques that recommend or suggest a particular product, service, or entity.

One other definition of a recommender system or a recommendation system (sometimes replacing "system" with a synonym such as platform or engine) is a subclass of [information filtering](https://en.wikipedia.org/wiki/Information_filtering_system) system that seeks to predict the "rating" or "preference" a user would give to an item.They are primarily used in commercial applications.
And one more simplest definition of recommendation is 

“Recommendation systems are systems that help users discover items they may like”


## Why Recommendation System ??
With increasing number of transactions happening over internet and with tremendous number of choices available to users, there is a need to sift and analyze relevant information on users and items. Recommendation systems exploit user preferences and traits to prioritize and recommend items which the users would like.

Recommendations systems are a big value-add for large companies like Google, Amazon, Facebook, Netflix etc. as they drive significant customer engagement and revenue. Analysts estimate that already 35% of what consumers purchase on Amazon and 75%of what they watch on Netflix come from product recommendations based on recommendation algorithms. Recommendation systems not only exploit users by tempting them to buy more products & services customized to their tastes, but also keep them engaged for a longer time to show them more ads and get more clients.
## Working of Recommender Systems
So how do recommender systems work? Let’s say Amazon wants to show you the top 10 recommendations in Books category. Here Amazon’s recommender system will start with some kind of data about you so as to figure out your individual tastes and interests. It will then merge this data about you with the collective behaviour of everyone else like you to recommend stuff you might like.
## Types of Recommendation System
 
 ![Type of Recommendation System](https://user-images.githubusercontent.com/19235560/61583026-e8eb1f80-ab4f-11e9-9f3b-0c827141a14f.png)

## Content Based Recommendation System
*Content-based filtering* involves recommending items based on the attributes of the items themselves. Recommendations made by content-based filters use an individual’s historical information to inform choices displayed. Such recommenders look for similarities between the items or products that a person had bought or liked in the past to recommend options in the future.

![Content base filtering](https://user-images.githubusercontent.com/19235560/61583152-c5c16f80-ab51-11e9-94e8-aec4b09f2fc1.png)

*Content based systems* use meta data such as genre, producer, actor, musician to recommend items say movies or music. Such a recommendation would be for instance recommending Infinity War that featured Vin Disiel because someone watched and liked The Fate of the Furious. Similarly you can get music recommendations from certain artists because you liked their music. Content based systems are based on the idea that if you liked a certain item you are most likely to like something that is similar to it.
## Colleborative Recommendation System

Collaborative filtering uses the combined power of ratings provided by many users/customers to present recommendations. It means recommending stuff based on other people’s collaborative behaviour.

![Colleborative filtering](https://user-images.githubusercontent.com/19235560/61583125-64010580-ab51-11e9-848d-b44f1331837c.png)

There are two approaches to collaborative filtering:
1. **Memory-based methods** which are also referred to as neighbourhood based collaborative filtering algorithms in which ratings of          user-item combinations are predicted on the basis of their neighbourhoods. These neighbourhoods can further be defined in one of        two ways:

    *User-based collaborative filtering*:
      In this model products are recommended to a user based on the fact that the products have been liked by users similar to the user. 
      For  example if Derrick and Dennis like the same movies and a new movie comes out that Derick likes,then we can recommend that           movie to Dennis because Derrick and Dennis seem to like the same movies.
    

    *Item-based collaborative filtering*:
      These systems identify similar items based on users’ previous ratings. For example if users A,B and C gave a 5 star rating to           books  X and Y then when a user D buys book Y they also get a recommendation to purchase book X because the system identifies book       X and Y as similar based on the ratings of users A,B and C. 
    
2. **Model-based methods** use machine learning methods to extract predictions for rating data by treating the problem as a normal            machine learning problem. Techniques like PCA, SVD, Matrix Factorisation, Clustering,
     Neural Nets etc can be used.
     Model-based methods are based on matrix factorization and are better at dealing with sparsity. They are developed using data            mining, machine learning algorithms to predict users’ rating of unrated items. In this approach techniques such as dimensionality        reduction are used to improve the accuracy. Examples of such model-based methods include decision trees, rule-based models,              Bayesian methods and latent factor models.
     
     
## Hybrid Recommendation System
Both Content-based and Collaborative approaches have their own strengths and weaknesses and one can end up with a better system by combining many algorithms together in what we call a hybrid approach. Hybrid systems leverage both item data and transaction data to give recommendations.

![hb](https://user-images.githubusercontent.com/19235560/61583280-8a27a500-ab53-11e9-9d20-eab8c80ef5f0.png)

A great example of using a Hybrid approach is that of Netflix. At Netflix, recommendations are not only based on what people’s watching and searching habits(collaborative systems)but also movies sharing similar characteristics(content-based) are also recommended.

