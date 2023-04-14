
## Audio Classification with PyTorch
This repository contains a PyTorch implementation of a multiclass image classification model trained on the PhysioNet/CinC 2016 dataset. The model uses a convolutional neural network (CNN) architecture to classify four different types of heart sounds: artifact, extrahls, murmur, and normal.

## Getting Started
To use this code, you will need to have PyTorch and torchvision installed. You can install them using pip:

pip install torch torchvision

The PhysioNet/CinC 2016 dataset should be downloaded and stored in two directories named "train" and "test", respectively. You can download the dataset from the PhysioNet website.

## Model Architecture
The model architecture is a simple CNN with two convolutional layers, two max pooling layers, and three fully connected layers. The input images are resized to 100x100 pixels and converted to grayscale. The final output layer uses a log softmax activation function to produce class probabilities.

## Training
The model is trained for 100 epochs using the Adam optimizer and cross-entropy loss function. The training loop iterates over the training data and updates the model parameters after each batch. The loss values are averaged over each epoch and plotted using seaborn.

## Testing
The trained model is tested on the test set and the accuracy is calculated using the sklearn.metrics.accuracy_score function. The confusion matrix is plotted using seaborn. The results show that the model achieves an accuracy of approximately 75%.

## Acknowledgments
This code is based on the PyTorch tutorial on image classification available on the PyTorch website. The PhysioNet/CinC 2016 dataset was provided by PhysioNet as part of a challenge to classify abnormal heart sounds.
