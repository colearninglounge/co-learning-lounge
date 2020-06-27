# Tutorial on Interpretability in AI 

# Decrytpting ML models using LIME - Workshop Condusted at PyConf Hyderabad, 2019

Instructor: Laisha Wadhwa

Time: 7th Dec 2019 04:00 – 05:30

With wide no. of libraries & frameworks available for building ML models ML has become a black-box these days. Thus model interpretability is vital. But its hard to define a model’s decision boundary in simple terms. **With LIME its easy to produce faithful explanations and decrypt any ML model.**

While model interpretability tricks like CV and grid search only answer the question from the perspective of the entire data-set. Feature importance explains this on data-set level which features are important in predicting the target. It allows you to verify hypotheses and whether the model is over fitting to noise, but it is hard to diagnose specific model predictions.

# Why should you use LIME?

If you are a novice or an expert in ML, LIME is just the tool for everyone. It explains a prediction so that even the non experts could compare and improve on an untrustworthy model through feature engineering. 
## LIME - an ideal model explainer

LIME is an ideal model explainer. Lets see how!
It uses a representation that is understood by the humans irrespective of the actual features used by the model. This is coined as interpretable representation. An interpretable representation would vary with the type of data we work with. For instance:
    - Text : It represents presence/absence of words.
    - Image : It represents presence/absence of super pixels ( contiguous patch of similar pixels ).
    - Tabular data : It is a weighted combination of columns.

Details on Hands on sessions:

Access [Google colab](https://colab.research.google.com/) and familiarize yourself with running code in the colab environment.

Read the 'Getting started' guide and go through the introductory video.


To run the notebooks open the link during the session and then select either of the two options:
<ul>
<li> Open in Playground mode.
<p align="center">
  <img src="/images/playground.PNG" width="350" title="hover text"/>
</p>

</li>
&nbsp;

<li> Save a copy in My drive and then run it in colab instance.
<p align="center">
  <img src="/images/saveCopy.PNG" width="350" title="hover text">
</p>
</ul>



1. [Digit classification using LIME](https://colab.research.google.com/drive/1WFGxoMV4UpIlqm1mw6Y2bBcr7G_44VbC#scrollTo=0LSML3Mr2cpF) : Understanding why we get false positives. Decrypting the decision boundary of Image classifiers.

2. [Text Analysis using LIME- Structured Data: ](https://colab.research.google.com/drive/1Od8jqECtBOcGrNpx_epo8NbY6N4lKUQH#scrollTo=OQN5tLu4DhFX)
: You'll be working with StackOverflow question and Tags data. After training a Logistic regression model you'll be understanding the importance of terms towards contributing the class of the tag.

3. Demo session on [Deep Learning models decrytion- cats and dogs classification using LIME](https://colab.research.google.com/drive/1kE3cOaVEIB-hK5IDMucNUJPF7MIaLSLP#scrollTo=aIkWfAsy1TjS)

All resources and further reading are added at the end of colab notebooks.

In case of any queries you can reach me on:
- Email: laisha.w16@iiits.in
- [Linkedin](https://in.linkedin.com/in/laisha-wadhwa-313b1212a)
- [Twitter](https:www.twitter.com/laishawadhwa)
