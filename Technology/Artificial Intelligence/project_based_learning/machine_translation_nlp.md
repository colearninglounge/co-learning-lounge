# <div align="center">Machine Translation</div>

> _“Words travel worlds. Translators do the driving”_ 
>  **-Anna Rusconi, Translator**

Well, there are roughly 6,500 languages spoken in the world today. Each one of them makes the world a diverse and beautiful place. Though language is indeed an art that must be mastered through hundreds and thousands of hours of practice. But with the advancement of technology like deep learning made the whole process damn simple and just one click away. 

![img]()

Machine Translation (MT) is the task of automatically converting one natural language into another, preserving the semantic meaning of the input text, and producing a fluent translation in the output language.

In this project-based learning, we will translate from German to English while building the end to end project from scratch with the step-by-step implementation of Deep Learning models in [Pytorch](http://pytorch.org/) along with exploring [Torchtext](https://pytorch.org/text/) and [Spacy](https://spacy.io/) library and creating [Streamlit](https://www.streamlit.io/) app(fastest and easiest way for data scientists to create beautiful, performant apps)

## <div align="center">Project Demo</div>

![demo]()


## <div align="center">Requirements</div>

- Basic knowledge of writing Python code.
- Basic knowledge of Data structures and Algorithms.
- Basic knowledge of NLP techniques like Tokenization, Word embeddings, Text classification, etc
- Machine Learning concepts (Feed Forward Layer, Training & Evaluation, Loss, Optimizers)
- Basic hands-on knowledge of PyTorch
- Should be familiar with version control tool like GitHub


## <div align="center">What will you learn?</div>

- Learn to collaboratively work on an open-source project using version control system(Git)
- This project will enable you to build simple to complex Natural Language Processing projects using the latest SOTA from Scratch and deploy as an app so that you can share with the world.
- Participating in this project will qualify you to join our intermediate and advanced projects on the same technology.
- Will gain confidence in reading and implementing research paper.
- Expand your peer group by connecting with like minded people.
- Guidance throughout the process by our mentors through daily status checks and sync up twice per week.
- You’ll be building a strong LinkedIn profile visible to recruiters.
- Learn about content creation and increase social media reach on LinkedIn to build your self-brand during the course(_If you are interested_)
- Get enough confidence to solve interview problems and technical interviews for Deep Learning role !!
- Learn documentation and blogging skills.

## <div align="center">Reading Material</div>

- If you are not familiar with Machine Learning Concepts means then go through [these tutorials by Deep Lizard](https://www.youtube.com/watch?v=gZmobeGL0Yg&list=PLZbbT5o_s2xq7LwI2y8_QtvuXZedL6tQU&index=1).
- We will be using Pytorch for the implementation. If you haven’t used PyTorch means then go through few [tutorials by Deep Lizard on Pytorch](https://www.youtube.com/watch?v=v5cngxo4mIg&list=PLZbbT5o_s2xrfNyHZsM6ufI0iZENK9xgG)
- Go through these [short tutorials on NLP zero to hero](https://www.youtube.com/watch?v=fNxaJsNG3-s&list=PLQY2H8rRoyvzDbLUZkbudP-MFQZwNmU4S) to understand the basic concepts in NLP like tokenization, word embedding, padding, RNN  (though it is in TensorFlow concepts remain the same in PyTorch)
- Word Embeddings
    * [Intuition and uses cases of Embeddings in NLP](https://www.youtube.com/watch?v=4-QoMdSqG_I)
    * The blog post of the above video ([The Illustrated Word2vec – Jay Alammar – Visualizing machine learning one concept at a time.](http://jalammar.github.io/illustrated-word2vec/))
- RNN and its variants will be used for translation tasks. Go through the following material to have a better understanding of what RNN’s are. 
    * [Colah Blog on Understanding LSTM](https://colah.github.io/posts/2015-08-Understanding-LSTMs/)
    * [Edwin Chen blog on Exploring LSTM](http://blog.echen.me/)
    * [Illustrated guide to LSTM and GRU - step by step explanation](https://towardsdatascience.com/illustrated-guide-to-lstms-and-gru-s-a-step-by-step-explanation-44e9eb85bf21)


# <div align="center">Course Outline</div>

## <div align="center"> Week 1: Creating a Basic Translation model using RNN (~3-4 hours) </div>

1. The process of converting textual data to tokens is called tokenization and is one of the most important steps in NLP. Learn the method to perform the tokenization:
    - spacy
    - torchtext

2. Machine Learning models do not process the text directly. Text needs to be converted into a numerical representation. There are various in which a text can be represented. Learn how to convert textual content to numerical format:
    - Word Embeddings

3. There are many problems where the sequence of nature needs to be remembered. For instance, in order to do the translation from one language to another, the model needs to remember the source sentence in-order to effectively translate into the target language. Learn how to use sequential models:
    - RNN

## <div align="center">Week 2: Improving the Translation model (~5 hours)</div>

In Phase 1, we have created a basic translation model. In this phase, we will try to improve it by trying different techniques.

1. There are a few problems involved in using the RNN (Vanishing and Exploding gradients). Learn how to mitigate these problems by using better RNN models.
    - LSTM
    - GRU

2. Improving the model by using attention mechanisms. The attention mechanism was born to help memorize long source sentences in neural machine translation (NMT). Rather than building a single context vector out of the encoder's last hidden state, attention is used to focus more on the relevant parts of the input while decoding a sentence. 
    - Bahdanau Attention

3. Not every sentence which needs to be translated is of the same length. Source language sentences could be of different lengths. Learn how to effectively feed the variable-length sentences to the model using the following techniques:
    - Packing padded sequences
    - Masking


## <div align="center">Week 3: Evaluating the Translation model & Visualizations (~4 hours)
</div>

1. A developed model needs to be evaluated for its performance before being actually deployed in a real-time environment. Learn the concepts to measure the performance of model-based on the following metric:
    - BLEU

2. A sentence can be translated in multiple ways. Learn the concepts to translate a sentence in different ways:
    - Greedy Search
    - Beam Search

3. Learn how to visualize which part of the sentence is given more preference while translating:
    - Attention Visualization

## <div align="center">Week 4: Building a Machine Translation App using Streamlit (~2 hours)</div>

1. Learn how to make an app using the pre-trained model (developed in Week 3) with streamlit.
2. Evaluating the model and hyperparameter tuning to improve the model.


# <div align="center">Further Improvements </div>

- Using sub-word tokenization methods like Byte-pair Encoding (BPE), Word Piece Encoding.
- Replace LSTM with advanced architecture: Transformer
- Using state-of-the-art model T5 for translation purposes.
- Can work on the same project for any language of choice.

# <div align="center">Post-course benefits</div>

-   Get your **GitHub** reviewed by experts.
-   Once you have undertaken and completed the project, you will get **full-fledged support from our mentors**, from the community for any technical help, guidance, etc.
- As most of the companies prefer giving assignments to the candidate for a DL role, we can help you to mentor for the same.
- As we have mentored and we know your skills and achievement, we will refer you for any AI/ML job which fits your profile.
- As we know LinkedIn is the platform to catch recruiters' attention, we will shout out your achievements, help to boost your work on LinkedIn to get visibility.

# <div align="center">Commitments from Learners</div>
- Since the project timelines are fixed, you will have to submit the assigned tasks and work within a given time.
- Please join based on your available bandwidth. Project fees are non-refundable.
- Classes will mostly be held during the weekends (Saturday, Sunday) for 2-3 hours per day.
- This project does not provide any certificate. Only **_certificates won't give you a job_**. Knowledge and projects will. That is what we primarily focus on **Hands-on projects**.

# <div align="center">How to apply?</div>

If you feel you are qualified and fit the requirements mentioned above, please send your profile (Resume, LinkedIn, GitHub) to colearninglounge@gmail.com with the subject line **Project-based project learning | NLP | Machine Translation**

While applying, do let us know:-

- Why do you want to join this project?
- What are your expectations for this project?

# <div align="center">Training period fee - ₹ 1999/- per person</div>

The project starts on 12th Aug 2020 till completion of the project OR 20th September 2020. Whichever comes first.

To maintain the quality of learning maximum 10 people in the batch is allowed.
The last day to apply is 9th Aug 2020.

For any query email us to colearninglounge@gmail.com.

# <div align="center">Scholarship opportunity</div>

During the span of the course, if you help us in creating content (learning material) for the course, then based on your contribution we will return the fees.

#### <div align="center">It's our sole decision about contribution and reward.</div>
