# Deep Learning: Image Classification using CNN
This project focuses on identifying and classifying potato diseases, specifically healthy, early blight, and late blight, using a Convolutional Neural Network (CNN). A common machine learning algorithm used for identifying human infections and diseases. My model achieves a predictive accuracy of 98% and utilizes Python, TensorFlow, Keras, Matplotlib, FastAPI, TF Serving, and Google Colab for various aspects of the project.

## Table of Contents
- [Introduction](#introduction)
- [Project Details](#project-details)
- [Usage](#usage)
- [Results](#results)

## Introduction

Potato farming is essential for food production worldwide. Identifying and classifying potato diseases early on is crucial for crop management and maximizing yield. This project leverages deep learning and CNNs to automate the process of identifying potato diseases, including healthy, early blight, and late blight.

## Project Details

- **Technology Stack:**
  - Python
  - TensorFlow
  - Keras
  - Matplotlib
  - FastAPI
  - TF Serving
  - Google Colab

- **Model Architecture:**
  - The CNN model includes additional layers for resizing, normalization, and data augmentation to enhance its performance.
  - It utilizes the Adam optimizer and the SparseCategoricalCrossentropy loss function for efficient training and accurate predictions.

- **Achieved Accuracy:**
  - The CNN model achieves a remarkable 98% predictive accuracy, making it highly reliable for potato disease classification.

- **Preprocessing with Google Colab:**
  - Google Colab is used for preprocessing tasks, ensuring high-quality input data for the model.

## Usage
1. Train the CNN model:
 - Run the training script to train the model using your dataset.
 - Adjust hyperparameters and model architecture as needed.

2. Start the FastAPI server:
 - Run the FastAPI server to expose the model's classification endpoint.

3. Use TF Serving:
 - Deploy the trained model using TF Serving for high-performance inference.

4. Access the API:
 - Access the classification API using the provided endpoint and send images for disease classification.

## Results
The model achieves an impressive 98% predictive accuracy, making it a valuable tool for potato farmers to detect diseases early and take necessary actions to protect their crops.
