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

# [Project 3. Netflix Suscription Fee (Data Visalisatiom)](https://github.com/Felixishabiyi/Data-Science-Projects/blob/main/Netflix%20Highest%20and%20Lowest%20Suscribing%20Countries.ipynb)
Netflix is a streaming service that offers a wide variety of award-winning TV shows, movies, anime, documentaries, 
and more on thousands of internet-connected devices.
Netflix is asssesible in 190 countries, as it can be Watch anywhere, anytime by signing in with your Netflix account to watch instantly on the web 
at netflix.com from your personal computer or on any internet-connected device that offers the Netflix app, including smart TVs, smartphones, tablets, 
streaming media players and game consoles. 
The Average cost of suscribing to the platform Worldwide is $15.32. 
This is a Data Visualizatio Project. My curosity on how netflix still find it hard to penetrate the ground roots to get more suscribers in Nigeria 
led me to get answers on Which countries pay the most and least for Netflix in 2021?
Data was obatined from [compatitech](https://www.comparitech.com/blog/vpn-privacy/countries-netflix-cost/) , The dataset conatains the following fields
Country, Total Library Size, No. of TV Shows, No. of Movies, Cost Per Month - Basic ($), Cost Per Month - Standard ($), Cost Per Month - Premium ($).

* Data was screening for missing values which was filled. After which was visualized using the heatmap plot albled by the seaborn library.
* Exploratory Data Analysis was done in order to understand relationship amongst the data. From which was deduced that the Total Library Size is 
highly correlated to the No of Movies. 
* Data Visualization was done using the seaborn library.
* From the barplot, it can be deduced that Croatia and SanMarino has the lowest library size with Croatia being the lowest of about < 2500 Movies
* From the second barplot, It was also deduced that the highest paying country as regards Cost Per Month - Premium ($) is Switzerland($28) while 
the lowest paying country is Turkey(<$5).
