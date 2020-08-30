# FAQ

Some common questions that were asked and needed to be answered.

## 1. What is MobileNet and why are we using it?

[MobileNet](https://arxiv.org/abs/1704.04861) is a pre-trained model available in TensorFlow JS. It has been trained using the [ImageNet dataset](http://www.image-net.org/).

They are small and low power models that can be used in places where computing resources are minimal.

They are also comparable to other popular large scale models like Inception.

![MobileNet](https://raw.githubusercontent.com/tensorflow/models/master/research/slim/nets/mobilenet_v1.png)

The size of the network in memory and on disk is proportional to the number of parameters. The latency and power usage of the network scales with the number of Multiply-Accumulates (MACs) which measures the number of fused Multiplication and Addition operations.

This makes MobileNet run efficiently on mobile devices and hence the name MobileNet.

In our project, we are using MobileNet and running it on the user's devices. So our model needs to be fast and accurate and should be able to run on less powerful CPUs.

So, MobileNet is the best choice.

## 2. What is a KNN Classifier?

Unlike MobileNet, the KNN Classifier available in TFJS is not pre-trained.

KNN model is based on the [K Nearest Neighbours](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm) algorithm. 

What we do in our project is we take the activations from the MobileNet model and we pass it to the KNN Classifier. We then train the KNN Classifier to map these activations to our custom labels.

So, essentially, we are only training the KNN Classifier.

We use the pre-trained MobileNet because they are good at extracting features from the images. And after that we can use these activations and classify them accordingly with the KNN Classifier.

## 3. What do you mean by "the activations from the MobileNet model"?

Since the MobileNet model is pre-trained, it is really good at extracting features from images. But it is trained only on some classes of images in the datasets and it can only directly classify the images into one of these classes.

But we need the model to detect our own classes. How can we do that?

We take the output of the model before the actual output often called as embedding. 

Think of it like this: The images are high dimensional vectors. When it is passed through the pre-trained model, the useful features, i.e the features that can be used to classify the images are extracted by the model. This is a low dimensional vector. This is then passed to the classifier.

## 4. Why do we use Bootstrap?

[Bootstrap](https://getbootstrap.com/) is the most popular HTML, CSS and JS library.

It is used for using pre-defined styles in your website.

In this project, we used Bootstrap to add styles. 

This is done using CSS.

Bootstrap already have implemented these styles which we import and use it in our project.

To do this we simply have to add the corresponding class name from the bootstrap documentation and the style corresponding to the class would be added to the HTML element.

Without Bootstrap we could have a style.css file and define these styles ourselves but since that is not part of our goal to learn TensorFlow JS, we use Bootstrap.
