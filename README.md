# Early Diabetes Classifier: Project Overview
This project uses artificial neural networks from Keras API to predict whether individuals show early sign of diabetes or not based on their charateristics.
* Create a tool that predict whether individuals will get diabetes or not 
* Optimized Keras classifier to reach the best model
## Code and Resources Used
* **Python Version:** 3.7
* **Packages:** pandas, numpy, matplotlib, seaborn, scikit learn
* **Kaggle Dataset:** https://www.kaggle.com/andrewmvd/early-diabetes-classification
## About The Data
The data contains the following columns:
* age
* gender
* polyuria : Whether the patient experienced excessive urination or not.
* polydipsia : Whether the patient experienced excessive thirst/excess drinking or not.
* sudden_weight_loss : Whether patient had an episode of sudden weight loss or not.
* weakness : Whether patient had an episode of feeling weak.
* polyphagia : Whether patient had an episode of excessive/extreme hunger or not.
* genital_thrush : Whether patient had a yeast infection or not.
* visual_blurring : Whether patient had an episode of blurred vision.
* itching : Whether patient had an episode of itch.

## EDA
I looked at the distributions of the data and the value counts for the various categorical variables. Below are a few highlights from the pivot tables.

![alt text](https://github.com/panasak/Deep-learning-placeholder/blob/main/eda/corr.png)
![alt text](https://github.com/panasak/Deep-learning-placeholder/blob/main/eda/count.png)
![alt text](https://github.com/panasak/Deep-learning-placeholder/blob/main/eda/dist.png)

## Model Building
First I transformed the categorical variable into dummy variables. I also scaled the data and split the data into train and test sets with a test size of 20%.
I used Keras API classifier as my model and evaluted the model using classification report and confusion metrics.

## Model Performance
The model performed well with the accuracy of 0.92
