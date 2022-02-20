# [Project 1. MelBourne House Prediction](https://github.com/Felixishabiyi/Data-Science-Projects/blob/main/MelBourne%20House%20Prediction%20Model.ipynb)
* This tool helps to predict the prices of houses (MAE ~ $23K) in Melbourne, Austrialia.
* Data was obatined from kaggle.com which was scraped from publicly available results posted every week from Domain.com.au.
* Relationships between columns was established and obsevered by performing data profiling.
* Decision Tree Regressor Model was adopted as the model. 

# [Project 2. Uber Price Prediction](https://github.com/Felixishabiyi/Data-Science-Projects/blob/main/Uber%20Price%20Prediction.ipynb)
Individuals will prefer to be pre-informed about the fare they will be paying per trip using a ride-hailing service(i.e Uber, Bolt).
This however made me to develop a tool that will predict the average amount an individual will be paying for using such service.
To Build this tool, data was obatined from kaggle.com. 
The dataset conatains the past records of all activities and transactions that have taken place on Uber Inc. 
Uber is one of the largest world's largest taxi company. 
The Dataset contains the follwoing fields.
key, fare_amount, pickup_datetime, passenger_count, pickup_longitude, pickup_latitude, dropoff_longitude, dropoff_latitude.

* Data Cleaning ; Filtering and finding values for the missing data was done using pythons numpy and pandas libraries.
* Feature Engineering was done inorder to fine tune the data and get an accurate output with the model.
* Exploratory Data Analysis was carried out inorder to establish relationships amongst the data.
* Data Visualization was done using cufflinks, seaborn and matplotlib 
* Using Scikit learn, Random Forest Regressor was adopted as the model of choice because of its extreme high accuracy as it also produces better result as compared linear regression.
* The score of the model was computed;
* Training score is: 0.6093692483788156
* Test score is: 0.554600748727676
