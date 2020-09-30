let classifier; // variable to store our model

let label = 'listening...'; // output listening as a placeholder

// Replace it with your own URL from https://teachablemachine.withgoogle.com/
let soundModel = 'https://teachablemachine.withgoogle.com/models/WSP4ifnt/';

// p5's preload() function is to load our model before we make predictions with it
function preload() {
  // Load the model from the URL using ml5's handy function soundClassifier()
  classifier = ml5.soundClassifier(soundModel + 'model.json');
}

// p5's setup() function has everything that runs just once
function setup() {
  createCanvas(320, 240); // create a canvas to print the predictions

  // Classify the audio using our model and call the gotResult function
  classifier.classify(gotResult);
}

// Draw or print the prediction of our model into the canvas
function draw() {
  background(0);
  fill(255);
  textSize(32);
  textAlign(CENTER, CENTER);
  text(label, width / 2, height / 2);
}

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