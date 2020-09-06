# Week 3

***Audio Classifier using p5.js and ml5.js***

This week we will look into [p5.js](https://p5js.org/) and [ml5.js](https://ml5js.org/) which will make using TensorFlow JS very easier if you are not a web dev.

By now, you have dug deep and wrote all the JavaScript code by yourself. But with the libraries like p5.js and ml5.js, it makes our lives easier.

We will train an Audio Classifier with [Google's Teachable Machine](https://teachablemachine.withgoogle.com/) and check how we can use it in our project.

![Preview](https://raw.githubusercontent.com/colearninglounge/co-learning-lounge/master/Technology/Artificial%20Intelligence/project_based_learning/teachable-machine-audio-classifier.gif)

### Step 1- Training the Audio Classifier

By now you must have been familiar with [Google's Teachable Machine](https://teachablemachine.withgoogle.com/).

Open a new Audio project.

You can add samples of different sounds and train the model.

Add the sample for background noise too so it can be differentiated. (Do not make a sound for sometime)

You can click the gear icon to configure the settings for recording audio. The more samples you add the better the model.

**This Audio Classifier is actually a image classifier. See all the waveform images when you record an audio, they are different for each sound clip and a image classifer is running in the background which classifies the sounds based on this waveform.***

After you have trained and tested your model, you can click the export model option and copy the sharable link. This would be used in our code when we create the web page using p5.js and ml5.js.

### Step 2- p5.js web editor

In this session, we will use [p5.js web editor](https://editor.p5js.org/) for writing our code.

It is really handy and has features like live preview which makes prototyping easier.

Check out this [video by Coding Train](https://www.youtube.com/watch?v=MXs1cOlidWs) on using the web editor.(Basic)

You can also follow up with [Cassie's tutorials](https://www.youtube.com/watch?v=x1rJJRVTpAI).

### Step 3- Creating the files

As always, we create an ```index.html``` and a ```sketch.js```(or ```script.js``` or anything else, name does not matter) file in the web editor.

### Step 4- The HTML code

```
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <title>Sound classification using TensorFlow JS</title>

  <!-- Load p5.js and ml5.js -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/0.9.0/p5.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/0.9.0/addons/p5.dom.min.js"></script>
  <script src="https://unpkg.com/ml5@latest/dist/ml5.min.js" type="text/javascript"></script>
</head>

<body>
  <script src="sketch.js"></script>
</body>

</html>
```

We will just import some scripts, namely, the p5.js and ml5.js library and the ```sketch.js``` file.

All the important code will go into the ```sketch.js``` file.

The completed code is available here- [index.html](https://gist.github.com/navendu-pottekkat/296a759c7a65d46ec2dcf5c47068994a), [sketch.js](https://gist.github.com/navendu-pottekkat/e782dde7cda2db1671d7c9bc36c6c4c2).

### Step 5- sketch.js

In the sketch.js we will first declare some constants.

```
let classifier; // variable to store our model

let label = 'listening...'; // output listening as a placeholder

// Replace it with your own URL from https://teachablemachine.withgoogle.com/
let soundModel = 'https://teachablemachine.withgoogle.com/models/WSP4ifnt/';
```

### Step 6- Loading the model 

We will now load the model from the URL above using the ```preload()``` function to make sure that the model is loaded before we start making predictions.

ml5.js has a ```soundClassifier()``` function that makes it easier for us to use the model without much configuration.

```
// p5's preload() function is to load our model before we make predictions with it
function preload() {
  // Load the model from the URL using ml5's handy function soundClassifier()
  classifier = ml5.soundClassifier(soundModel + 'model.json');
}
```

### Step 7- Start drawing

In p5.js, the web page is treated as a canvas where we can literally draw. We will create a canvas first.

In p5.js, everything that runs once is added inside the ```setup()``` function.

We just have to call the ```classify()``` function to make predictions with our model.

```
// p5's setup() function has everything that runs just once
function setup() {
  createCanvas(320, 240); // create a canvas to print the predictions

  // Classify the audio using our model and call the gotResult function
  classifier.classify(gotResult);
}
```

Draw!

```
// Draw or print the prediction of our model into the canvas
function draw() {
  background(0);
  fill(255);
  textSize(32);
  textAlign(CENTER, CENTER);
  text(label, width / 2, height / 2);
}
```

Try tweaking this function after you have implemented everything and figure it out.

### Step 8- Draw the predictions

We will get the label from the results and add an emoji key for fun.

The value of the label will get drawn by the ```draw()``` function.

```
// When the model makes a prediction, this function gets the predicted label to be drawn on the canvas
// Also, in the case of any errors, it will log the error in the console
function gotResult(error, results) {
  if (error) {
    console.error(error);
    return;
  }
  // The predictions are in an array in the order of confidence
  // The first element of the array would be the prediction with the maximum confidence
  label = results[0].label;

  // Add emojis with our labels just for fun!
  if (label == "Whistles") {
    label = "Whistle 😗"
  }
  else if (label == "Claps") {
    label = "Clap 👏"
  }
  else if (label == "Snaps") {
    label = "Snap 🤏"
  }
}
```

Hit play and test if it is working!

You can now share the live link!
