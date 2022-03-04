# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 20:31:51 2022

@author: Oluwasegun
"""

import numpy as np
import pickle
import streamlit as st

loadhm = pickle.load(open('C:/Users/Administrator/Documents/Data science P/Heart Disease App/trained_model.sav','rb'))

# creating a function for prediction

def heart_disease_prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loadhm.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
        return 'The person is free from heart disease'
    else:
        return 'The person is likely to develop heart disease'
  
    
def main():
      
    #title
    st.title('Heart Disease Prediction Web App')
       
    # getting the input data from the user
      
    age = st.text_input('Age of the Patient in Years')
    sex = st.text_input('Sex of the Patient')
    cp = st.text_input('Chest Pain Accoriding to level')
    trestbps = st.text_input('Resting blood pressure')
    chol = st.text_input('Serum Cholesterol Level')
    fbs = st.text_input('Fasting blood sugar > 120 mg/dl')
    restecg = st.text_input('Resting electrocardiographic results (values 0,1,2)')
    thalach = st.text_input('Maximum heart rate achieved')
    exang = st.text_input('Exercise induced angina')
    oldpeak = st.text_input('Oldpeak = ST depression induced by exercise relative to rest')
    slope = st.text_input('The slope of the peak exercise ST segment')
    ca = st.text_input('Number of major vessels (0-3) colored by flourosopy')
    thal = st.text_input('Thal: 3 = normal; 6 = fixed defect; 7 = reversable defect')
      
      
    # code for prediction
      
    diagnosis = ''
      
     # creating a button for prediction
      
    if st.button('Heart Disease Test Result'):
        diagnosis = heart_disease_prediction([age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal])
          

    st.success(diagnosis)
      
      
      
      
if __name__=='__main__':
    main()