# [Project 1. MelBourne House Prediction](https://github.com/Felixishabiyi/Data-Science-Projects/blob/main/MelBourne%20House%20Prediction%20Model.ipynb)
### Data Collection
The Data obtained from kaggle.com, It was Initially was scraped from publicly available results posted every week from Domain.com.au.

### Data Discovery and Profiling
Exploratory Data Analysis was perfromed on the data in order to understand what the data, what needs to be done and adjusted in order to prepare it for the intended uses.
Data was correlated with the price inorder to deduce which columns influences price.
Jointplot, Distplot was carried out on the data inorder to determine relationships.

### Data Cleaning
Missing values was detected using .isnull() function called on the data which was then visualized using seaborns heatmap.
Columns were dropped and columns with missing values were filled.

### Machine Learning
Train Test Split was imported using scikit learn model selection
Decision Tree Regressor was adopted for the Machine learning Process.
Fitting and Testing of the model was done.
Model was Validated using scikitlearn metrics;
The Mean Absolute Error is 238530.794059892 while the Mean Squared Error is 167984881597.42587
