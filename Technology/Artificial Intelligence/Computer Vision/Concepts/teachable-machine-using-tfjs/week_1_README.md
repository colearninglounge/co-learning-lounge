# Before starting

Some stuff to go through before building the Teachable Machine:

* **[Teachable Machine](https://teachablemachine.withgoogle.com/)**: Try it out with your own data.
* **[Absolutely never seen HTML code](https://www.yourhtmlsource.com/myfirstsite/myfirstpage.html)**: We won't build super complex websites so a basic idea about different tags is enough.
* **[Try some JavaScript](https://www.w3schools.com/html/html_scripts.asp)**.
* **TensorFlow**: If you have never used TensorFlow or are new to ML, Transfer Learning or Computer Vision:
    * [Hello World!](https://towardsdatascience.com/hello-world-for-machine-learning-4dc9af0a7430)
    * [Computer Vision](https://towardsdatascience.com/classifying-fashion-apparel-getting-started-with-computer-vision-271aaf1baf0)
    * [Convolutional Neural Networks](https://towardsdatascience.com/classifying-fashion-apparel-getting-started-with-convolutional-neural-networks-3ae4fc5d9f76)
    * [Transfer Learning](https://codelabs.developers.google.com/codelabs/keras-flowers-transfer-learning/)
* [**Optional**] **[Check out p5.js](http://p5js.org/)**- We will only be using some basic stuff.

# Week 1

***Creating the web interface using HTML***

We will first make a front-end for our Teachable Machine. We will use HTML and some [Bootstrap](https://getbootstrap.com/) styles for making the interface.

[Bootstrap](https://getbootstrap.com/) is a front end toolkit that lets us easily style web pages. Since we are more focused on TensorFlow JS, we can leave the heavy front-end design stuff to Bootstrap.

This is also a great tool in your arsenal for future projects.

We will learn how to use Bootstrap as we build the front-end.

The complete code for this session can be found on this [Gist](https://getbootstrap.com/).

## Step 1- Create an index.html file

```index.html``` is the homepage for your websites. When a website is loaded this is the page that is loaded in the browser.

Open a file in your code editor and name it ```index.html```

## Step 2- Import libraries

First we will load external libraries to be used in our project- TensorFlow JS, Bootstrap and the two models MobileNet and KNN Classifier.

```
<!DOCTYPE html>
<html lang="en">

<head>
   <meta charset="UTF-8">
   <meta name="viewport" content="width=device-width, initial-scale=1.0">
   <title>Teachable Machine Using TensorFlow JS</title>

   <!-- Load the latest version of TensorFlow.js -->
   <script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs"></script>
   <!-- Load the MobileNet model -->
   <script src="https://cdn.jsdelivr.net/npm/@tensorflow-models/mobilenet"></script>
   <!-- Load KNN Classifier model -->
   <script src="https://cdn.jsdelivr.net/npm/@tensorflow-models/knn-classifier"></script>

   <!-- We will use some Bootstrap to style our page easily -->
   <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css"
       integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
</head>
```

## Step 3- Create the body of the page

We will add a Navbar with a title for our project using Bootstrap.
```
<body>
   <!-- Add a Navbar with a title -->
   <nav class="navbar navbar-dark bg-primary">
       <span class="navbar-brand mb-0 h1">Teachable Machine Using TensorFlow JS</span>
   </nav>

We will then add a console to display the predictions. 

  <!-- Wrap everything into a container -->
   <div class="container">
       <!-- We will add a console area to display the prediction of the model -->
       <div class="row d-flex justify-content-center text-center">
           <strong>
               <div class="col" id="console"></div>
           </strong>
       </div>
```

Below that we will add a window to display the feed from the webcam.

```
       <!-- Add a window to display the video from the webcam -->
       <div class="row d-flex justify-content-center text-center">
           <video class="col m-4 p-1" autoplay playsinline muted id="webcam" width="224" height="224"></video>
       </div>
```

Next we will add 3 textboxes and buttons for adding training images to our model.

```
<!-- Add a window to display the video from the webcam -->
       <div class="row d-flex justify-content-center text-center">
           <video class="col m-4 p-1" autoplay playsinline muted id="webcam" width="224" height="224"></video>
       </div>
       <!-- Add three buttons and text boxes for adding training images -->
       <div class="row d-flex justify-content-center text-center">
           <div class="col-sm m-2">
               <button class="btn btn-primary" id="class-a">Add A</button>
               <input type="text" placeholder="Enter label for object A" id="a">
           </div>
           <div class="col-sm m-2">
               <button class="btn btn-primary" id="class-b">Add B</button>
               <input type="text" placeholder="Enter label for object B" id="b">
           </div>
           <div class="col-sm m-2">
               <button class="btn btn-primary" id="class-c">Add C</button>
               <input type="text" placeholder="Enter label for object C" id="c">
           </div>
       </div>
   </div>
```

## Step 4- Import our JS file

We do not have a JS file yet. We will cover that in the next phase.

We can just add an import to script.js file which we will make later.

```
   <!-- Load script.js after the page content has been loaded -->
   <script src="script.js"></script>
</body>

</html>
```

That is it! Now you have the UI for our Teachable Machine. 

Next week, we will start building the brain of our project using TensorFlow JS.
