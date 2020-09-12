# Week 4

***Taking it ahead!***

By now we have 2 working TFJS projects on the Internet that anyone can use. How can we improve this? What else can we do with TFJS to improve our project?

This week we will look into all these.

### Converting models to TFJS

Usuall we may have models elsewhere that we want to use in web apps. So, we need some way to convert those models to TFJS.

Luckily, this is easy as TensorFlow JS provides a [model converter](https://github.com/tensorflow/tfjs/tree/master/tfjs-converter) for this purpose.

If you have a Keras model saved in .h5 format and if you want to use the model for your web app, you have to covert it into TFJS model.

If the model is saved as ```model.h5```, to convert it to TFJS format, we do something like this.

```
$ tensorflowjs_converter --input_format=keras /tmp/model.h5 /tmp/tfjs_model
```

This will convert the model at /tmp/model.h5 and output a ```model.json``` file along with binary weight files to your ```tmp/tfjs_model/``` directory.

You can check this [doc from TensorFlow](https://www.tensorflow.org/js/guide/conversion) and this [article by Paul](https://dev.to/paulsp94/convert-keras-models-to-tfjs-2k3).

Try creating a model --> Save it --> Convert to TFJS --> Use it in a web app.

You are already familiar with using the model in the web app. Try this out.

You can even try the web cam approach to test a pre-trained model. You can check [this guide](https://www.tensorflow.org/js/tutorials/conversion/import_keras) for more info.

### Creating models using the layers API

We have not looked how we can use layers API from TensorFlow to create models from scratch. We have only used pre-trained models or models trained elsewhere till now. The code we use to train the model in Python is similar to the code in JavaScript as shown below:

**Python code**
```
# Python:
import keras
import numpy as np

# Build and compile model.
model = keras.Sequential()
model.add(keras.layers.Dense(units=1, input_shape=[1]))
model.compile(optimizer='sgd', loss='mean_squared_error')

# Generate some synthetic data for training.
xs = np.array([[1], [2], [3], [4]])
ys = np.array([[1], [3], [5], [7]])

# Train model with fit().
model.fit(xs, ys, epochs=1000)

# Run inference with predict().
print(model.predict(np.array([[5]])))
```

**JavaScript Code**

```
// JavaScript:
import * as tf from '@tensorlowjs/tfjs';
// We have not used the above line in our projects since we import TensorFlow JS using the script tag in the HTML file,
// This import is only needed when we install tfjs using NPM which is beyond the scope of our sessions.

// Build and compile model.
const model = tf.sequential();
model.add(tf.layers.dense({units: 1, inputShape: [1]}));
model.compile({optimizer: 'sgd', loss: 'meanSquaredError'});

// Generate some synthetic data for training.
const xs = tf.tensor2d([[1], [2], [3], [4]], [4, 1]);
const ys = tf.tensor2d([[1], [3], [5], [7]], [4, 1]);

// Train model with fit().
await model.fit(xs, ys, {epochs: 1000});

// Run inference with predict().
model.predict(tf.tensor2d([[5]], [1, 1])).print();
```

You can check this [doc](https://www.tensorflow.org/js/guide/layers_for_keras_users) to get an intuitive understanding of the differences.

You can check the guides below for more about TFJS:
* [Models and layers](https://www.tensorflow.org/js/guide/models_and_layers)
* [Training models](https://www.tensorflow.org/js/guide/train_models)
* [Saving and Loading models](https://www.tensorflow.org/js/guide/save_load)

You can also try building a Convolutional Neural Network like you have build with Keras in TensorFlow JS. This [code lab](https://codelabs.developers.google.com/codelabs/tfjs-training-classfication/index.html#0) will walk you through it. 

Since this is already familiar to you with Python, using similar approach in JavaScript will work.

### Contributing back

By now you have learned the essentials of TensorFlow JS. These are the underlying ideas of every project using TensorFlow JS. 

You have also learned how you can use web dev tools and libraries to build applications around your TFJS models. You are also familiar with libraries like p5.js and ml5.js which makes your work easier.

The only way to train these skills is by building things on your own. Since we have two working projects, with us which are very crude and basic, there is a lot of room for improvement. 

Till now, you had the code that you can look into and by now I beleive that you are comfortable with TFJS enough to build things on your own. 

With the basics down and with all the other resources available online, you can build things and with the mentorship available always, you will be able to clarify things when you are stuck.

Some of the changes to the project I think would be great are follows:

**Teachable Machine using TFJS**

* **Add more teachabe models like in [Google's Teachable Machine](https://teachablemachine.withgoogle.com/)**- We can add more models to our Teachable Machine like Pose Estimation. We can even go beyond the Google's version and add even more Teachable Machines to make it kind of even better than Google.

* **Add option to save model**- For now our Teachable Machine does not have an option to save the model to be used later. We can add a feature that lets users to train and download the model to be used in their own projects.

**Audio Classifier**

* **Improve GUI**- We can improve the GUI of our app into something more like [this](https://tm-audio-demo.glitch.me/)

These are just some ideas that I think can improve the project. If you have your own ideas you can implement that too.

### Learning from projects

By now you would agree that doing things is the best way to learn and building projects is the best way to learn a new topic.

We have deliberately built a relatively simple project just so that you have a firm grasp about the basics.

If we started with a complex project, you will be overwhelmed and would end up just copying the code. 

With the knowledge you have now about TFJS you would be able to build complex projects on your own. 

Here is a [project I am working on](https://github.com/nsfw-filter/nsfw-filter) with TFJS. 

It is a browser extension that uses TFJS to detect innapropriate images(NSFW images) and block them. It has a tfjs model which has been pre-trained and converted to tfjs format.

As you can see from the code, there is a lot of moving parts and if I try to teach you something like that, it will only make you more confused.

But if you look at the code from maybe [the first realease](https://github.com/nsfw-filter/nsfw-filter/archive/v0.2-beta.zip), it is still a lot but you can see clearly how we have used TFJS.

I would suggest you to go through the projects and try and build something like that on your own by which you learn.

It took me 1 month to even release the beta version full of bugs after starting the project. There was not enough docs to how to use tfjs models with a web extension. I had to go through a lot of articles, talk to a lot of people before figuring out how to do that.

So my suggestion to learning more is start with what you know. As you progress with your project learn new things and build them. Check a lot of projects and try to implement that.

Here are some projects from which you can learn-

* [NSFW Filter](https://github.com/nsfw-filter/nsfw-filter)- This is my project(check above for more info) and I would suggest you to check the [earlier version](https://github.com/nsfw-filter/nsfw-filter/releases/tag/v0.2-beta) of the code to get started.

* [Object Detection in browser using TFJS](https://github.com/navendu-pottekkat/tfjs-object-detection)- A real-time object detection model in the browser using COCO-SSD.

* [Emoji Scavenger Hunt](https://github.com/google/emoji-scavenger-hunt)- Emoji Scavenger Hunt is an experiment that leverages the power of neural networks and your phone’s camera to identify the real world versions of the emojis we use every day.

* [Teachable Machine Starter projects](https://glitch.com/@teachablemachine/teachable-machine-starter-projects)- A set of starter projects for models created with Teachable Machine.

* [Tic-Tac-Toe AI](https://github.com/GantMan/tictactoe-ai-tfjs)- Train your own TensorFlow.js Tic Tac Toe created by Gant Laborde. Also checkout his other projects.

* [TFJS projects in glitch](https://glitch.com/@TensorFlowJS)- Jason has built many TFJS projects from easy to advanced levels. All the code is open-source and with your prior knowledge you can easily build these projects. These are also available in [codepen.io](https://codepen.io/topic/tensorflow/templates).

* [Virtual Tailor](https://www.youtube.com/watch?v=kFtIddNLcuM) - Get an estimate of your clothing size measurements in less than 15 seconds.

* [Invisibility Cloak](https://github.com/jasonmayes/Real-Time-Person-Removal) - Bring your scifi movie dreams to life with this real time person removal system that runs in the browser.

* [Move Mirror](https://experiments.withgoogle.com/collection/ai/move-mirror/view) - An AI Experiment with Pose Estimation in the Browser using TensorFlow.js

* [Arbitrary style transfer using TensorFlow.js](https://github.com/reiinakano/arbitrary-image-stylization-tfjs)- Implementation of arbitrary style transfer running fully inside the browser using TensorFlow.js.

* [Tensorflow JS - Rock Paper Scissors](https://github.com/GantMan/rps_tfjs_demo)- Training a Rock Paper Scissors model in the browser via TFJS.

I urge you to try building things that you find interesting on your own.

These are some of the stuff I found interesting. You can follow the hashtag #MadeWithTFJS in Twitter and LinkedIn for more projects.

You can also try contributing to these projects if they are open-source.

### Winding up and next steps

By now you would have hands-on experience with TensorFlow JS. You would be able to use that skills to build projects like the one above.

You can now contribute back to our project and make it even better. With all these resources and skills you would be able to do that.

Here are some additional resources that you can check to take things to the next level-

* **Javascript Learning resources**-
  * [freeCodeCamp](https://www.freecodecamp.org/)
  * [w3schools.com](https://www.w3schools.com/js/)
  * [tutorialspoint](https://www.tutorialspoint.com/javascript/index.htm)
* **p5.js and ml5.js**
  * [Programming with p5.js with The Coding Train](https://www.youtube.com/playlist?list=PLRqwX-V7Uu6Zy51Q-x9tMWIv9cueOFTFA)
  * [Beginners Guide to Machine Learning in JavaScript](https://www.youtube.com/playlist?list=PLRqwX-V7Uu6YPSwT06y_AEYTqIwbeam3y)
  
This is not an exhaustive list, if you need more resources let me know and I will share some resources.

**Happy learning! We hope you will be able to contribute to the projects.**
