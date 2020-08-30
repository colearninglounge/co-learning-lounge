# Week 2

***Creating the brain- script.js***

By now, you will have the HTML page ready for your Teachable Machine.

Now it is time to roll up our sleeves and get coding with TensorFlow JS. 

We will be using plain JavaScript to code. You will have a more concrete understanding of TensorFlow JS this way.

The complete code for this section is available [here](https://gist.github.com/navendu-pottekkat/3204ee775a20f6e7457415a2c228fcd2).

## Section summary

* Load the models(MobileNet and KNN).
* Get video stream from webcam.
* Train the model with the images from the webcam.
* Perform inference with the model.

## Step 1- Create script.js file

Create a ```script.js``` file in the same directory as your ```index.html``` file.

This is the file where we will be writing our JavaScript code.

## Step 2- Initialise variables and import the classifier

```
const webcamElement = document.getElementById('webcam'); // get the webcam element line-36

const classifier = knnClassifier.create(); // load the KNN Classifier model l-14

let net; // initialise a variable to hold the MobileNet model
```

We first get the ```webcamElement``` that we defined in the HTML file.

## Step 3- Load the MobileNet model

```
async function app() {
    // When the script is loaded, the function app would be run
    console.log('Loading mobilenet..'); // To check for errors let's log some info to the console

    // Load the MobileNet model
    // Notice that we are using the await keyword so the execution of the script is not interrupted
    net = await mobilenet.load();

    console.log('Successfully loaded model');
```

The ```app()``` function will contain everything to be run in the background.

We will first load the MobileNet model and the ```console.log()``` is to just for debugging.

## Step 4- Get the webcam stream

```
    // TensorFlow JS has this handy API that lets us create Tensors from the webcam video stream
    // Since TensorFlow models use Tensors we will use this API
    const webcam = await tf.data.webcam(webcamElement); // get webcam stream as Tensors
```

As written in the comments, we will get the stream from the webcams as Tensors(fancy name for a multidimensional matrix), as they are the best when it comes to working with TensorFlow.

## Step 5- Function to "train" our model

```
    // Funnction to read an image from the webcam and associate it to a specific class
    const addExample = async classId => {
        // Get an image from the web cam video stream
        const img = await webcam.capture();

        // Get the activation from the MobileNet model and pass it to the KNN Classifier
        const activation = net.infer(img, true);

        // Pass the activation to the KNN Classifier
        classifier.addExample(activation, classId);

        // Dispose the tensor to release the memory
        img.dispose();
    };

```

This is how we plan to teach the machine:
* First we have the MobileNet model.
* We will pass the image Tensor to the MobileNet model and get its activation
* Since the MobileNet model is pre-trained, we will get some good results.
* We will then pass this activation to a KNN classifier which will be the part which we train.
* We will use the ```addExample()``` function to add training images of a particular class.
* We will then dispose the image to release the memory.

Now we will call this function everytime the button is pressed.

## Step 6- Teaching the machine

```
    // Add samples of particular class on the corresponding button press
    document.getElementById('class-a').addEventListener('click', () => addExample(0)); // adds samples of object A
    document.getElementById('class-b').addEventListener('click', () => addExample(1)); // adds samples of object B
    document.getElementById('class-c').addEventListener('click', () => addExample(2)); // adds samples of object C

```

We will add samples of the corresponding classes on each button press.

```
    // Make predictions on our trained model
    while (true) {
        if (classifier.getNumClasses() > 0) {
            // Get an image from the web cam video stream
            const img = await webcam.capture();

            // Get the activation from the MobileNet model and pass it to the KNN Classifier
            const activation = net.infer(img, 'conv_preds');

            // Get the prediction from the Classifier
            const result = await classifier.predictClass(activation);

            // Get label names from the text fields
            const classes = [document.getElementById('a').value, document.getElementById('b').value, document.getElementById('c').value];

            // Output the predictions to the console l-31
            document.getElementById('console').innerText = `
          Prediction: ${classes[result.label]}\n
          Probability: ${result.confidences[result.label]}
        `;

            // Dispose the tensor to release the memory
            img.dispose();
        }

        await tf.nextFrame();
    }
}

app();
```

We will now run the trained model to get predictions.

We will pass the image Tensor to the classifier --> Get the activation --> Pass the activation to our KNN Classifier to get predictions.

We will then print the output to the console element which we defined in the HTML file.

Finally we will call the ```app()``` function to run everything.

**That is it!**

Open the ```index.html``` file in the browser of your choice.

You will be prompted to allow access to your camera.

Try teaching your model different stuff and see how it performs and how many samples does it take to get good results.

## Step 7- Deploying it to the Internet

Deploying Machine Learning models to the Internet seems like a tedious task.

Surely we would need some backend server running hosting all the models and performing the training and inference. Right?

**Wrong!** We can host the website as a static website for free using GitHub pages. 

The model will not run on the server but on each user's browser. Isn't that neat?

**How to deploy to GitHub pages?**
* Upload the local files to a GitHub repository.
* Go to settings--> Scroll down to GitHub pages.
* Choose the branch you want to deploy.
* It will automatically detect the index.html file and it will show the link to the website.
* Enforce HTTPS for security.

You can now share this with anybody over the Internet!

Share away!
