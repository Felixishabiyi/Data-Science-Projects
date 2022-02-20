# [Project 1. MelBourne House Prediction](https://github.com/Felixishabiyi/Data-Science-Projects/blob/main/MelBourne%20House%20Prediction%20Model.ipynb)
Getting an apartment is a daunting task, as a lot of questions begins to pop in one's mind, one of which is the average price to get an apartment in a particular area, city or country.
To get an answer to this question the moments it pops in one's mind, I decided to developed a machine learning model that predicts the total cost to get an apartment in MelBourne, Austrailia.
The data was obained from Kaggle.com, the data was scraped from publicly available results posted every week from Domain.com.au which was also has 
been cleaned.
The dataset contains the follwoing fields; 
Rooms, Price, Method, Type, Seller, Date, Distance, Regionname, Propertycount, Bedroom, Bathroom, Car, Landsize, BuildingArea, CouncilArea.

* Exploratory Data Analysis was performed inorder get the right features which influences the prices of an apartment. The major influence was the number of rooms which was correlated at 0.49. 
* The YearBuilt, CouncilArea, BuildingArea Columns were deleted as it was not correlated as highly as the number of rooms. 
* The YearBuilt and BuildingArea Columns were coreelated at -0.323617 and 0.090981 respectively.
* Using Scikit Learn, Decison Tree Regressor was adopted as the model to be used in the prediction of apartment prices.
* The model was validated using Metrics from scikit learn. 
* The Mean Absolute Error: 238530.794059892
* The Mean Squared Error 167984881597.42587 

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
* Training score: 0.6093692483788156
* Test score: 0.554600748727676
