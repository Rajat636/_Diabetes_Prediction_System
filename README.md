
# Diabetes Prediction and Recommendation System




## Table Of Contents

- Introduction

- Data Collection 
- Data Preprocessing
- Exploratory Data Analysis
- Modeling
- Results

# Introduction
The Diabetes Prediction and Recommendation System is designed to predict the likelihood of a patient having diabetes based on their medical attributes. This project employs machine learning models to analyze data and provide predictions. The user interface is built using the Streamlit Python library for ease of use.



## Data Collection
Data is collected from kaggle



## Data Preprocessing

Data preprocessing steps include:

Handling missing values
Encoding categorical variables
Normalizing numerical features
Splitting the data into training and testing sets


## Exploratory Data Analysis

Exploratory Data Analysis (EDA) was performed to understand the dataset better and to identify patterns and correlations. Key steps in EDA include:

Visualizing the distribution of features
Analyzing the correlation between features
Identifying any outliers or anomalies

## Modeling
Three machine learning models were used for prediction:

ExtraTree Classifier
XGBoost Classifier
GradientBoosting Classifier
The steps involved in modeling were:

Training the Models: Each model was trained on the preprocessed training data.
Evaluating the Models: Models were evaluated using accuracy, precision, recall, and F1-score.
Selecting the Best Model: The model with the highest accuracy was selected to create pickle file for creating user interface.

## Results
The ExtraTree Classifier achieved the highest accuracy among the three models. Here are the accuracy scores:

ExtraTree Classifier: 92%
XGBoost Classifier: 91%
GradientBoosting Classifier: 91%