const webcamElement = document.getElementById('webcam'); // get the webcam element line-36

const classifier = knnClassifier.create(); // load the KNN Classifier model l-14

let net; // initialise a variable to hold the MobileNet model

async function app() {
    // When the script is loaded, the function app would be run
    console.log('Loading mobilenet..'); // To check for errors let's log some info to the console

    // Load the MobileNet model
    // Notice that we are using the await keyword so the execution of the script is not interrupted
    net = await mobilenet.load();

    console.log('Successfully loaded model');

    // TensorFlow JS has this handy API that lets us create Tensors from the webcam video stream
    // Since TensorFlow models use Tensors we will use this API
    const webcam = await tf.data.webcam(webcamElement); // get webcam stream as Tensors

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

    // Add samples of particular class on the corresponding button press
    document.getElementById('class-a').addEventListener('click', () => addExample(0)); // adds samples of object A
    document.getElementById('class-b').addEventListener('click', () => addExample(1)); // adds samples of object B
    document.getElementById('class-c').addEventListener('click', () => addExample(2)); // adds samples of object C

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