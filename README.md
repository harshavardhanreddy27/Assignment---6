# Assignment---6
Neural Networks &amp; Deep Learning Assignment - 6
### Question 1b
The script brings in necessary tools like pandas for handling data, scikit-learn for data prep and model selection, and TensorFlow for creating neural networks.It reads breast cancer data from a CSV file called 'breastcancer.csv' into a pandas DataFrame.It displays the first few rows of the DataFrame to check how the data looks after preprocessing.
### Question 1a
Extract features (`X`) by removing 'id' and 'diagnosis' columns.Assign labels (`y`) from the 'diagnosis' column.Train the model on the training data for 10 epochs, using batches of 32 samples. Validate performance during training using validation data.Assess the model's accuracy on the test data and display the result.
### Question 1c
The features are normalized using StandardScaler to standardize their distribution.A neural network (`model_task3`) is created with two hidden layers of 32 and 64 neurons respectively, using ReLU activation. The output layer has one neuron with a sigmoid activation for binary classification.Trained on the normalized training data for 10 epochs with a batch size of 32.The accuracy of the normalized model is evaluated on the test data and printed out.
### Question 2a
The code loads the MNIST dataset, containing handwritten digit images, and preprocesses them by scaling the pixel values to the range [0, 1]. 9.The model is trained on the training images and labels for 10 epochs, with validation data provided for monitoring.The training and validation loss and accuracy are plotted over epochs using matplotlib, providing insights into the model's performance.
### Question 2b
The code visualizes a specific test image from the MNIST dataset using matplotlib. The image is displayed in grayscale, and its true label is shown as the title.It selects an image from the test set for prediction.
### Question 2c
The modified model (`modified_model`) has a similar architecture to the previous model, with some changes in activation functions and layer sizes.The first dense layer has 128 units with tanh activation, and the second layer has 10 units with softmax activation for classification.Training is performed on the MNIST training dataset for 10 epochs, with validation data provided for monitoring.The training and validation loss and accuracy are plotted over epochs using matplotlib, providing insights into the performance of the modified model.
### Question 2d
Ensure you have the MNIST dataset available. The dataset can be loaded using `mnist.load_data()` provided by TensorFlow or Keras.The model architecture is defined using the Keras Sequential API.The modified model (`model_no_scaling`) comprises several layers.

### Video Link
https://drive.google.com/file/d/1zjrASy8DHu_a4HS3j16pS7lXlxCY9ds8/view?usp=share_link
