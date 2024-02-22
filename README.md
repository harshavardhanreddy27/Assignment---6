# Assignment---6
Neural Networks &amp; Deep Learning Assignment - 6
### Question 1b
The script brings in necessary tools like pandas for handling data, scikit-learn for data prep and model selection, and TensorFlow for creating neural networks.It reads breast cancer data from a CSV file called 'breastcancer.csv' into a pandas DataFrame.It displays the first few rows of the DataFrame to check how the data looks after preprocessing.
### Question 1a
Extract features (`X`) by removing 'id' and 'diagnosis' columns.Assign labels (`y`) from the 'diagnosis' column.Train the model on the training data for 10 epochs, using batches of 32 samples. Validate performance during training using validation data.Assess the model's accuracy on the test data and display the result.
### Question 1c
The features are normalized using StandardScaler to standardize their distribution.A neural network (`model_task3`) is created with two hidden layers of 32 and 64 neurons respectively, using ReLU activation. The output layer has one neuron with a sigmoid activation for binary classification.Trained on the normalized training data for 10 epochs with a batch size of 32.The accuracy of the normalized model is evaluated on the test data and printed out.
### Question 2a
