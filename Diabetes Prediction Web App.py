# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 14:21:58 2022

@author: Oluwasegun
"""

import numpy as np
import pickle
import streamlit as st

loadm = pickle.load(open('C:/Users/Administrator/Documents/Data science P/Diabetes App/trained_model.sav','rb'))

# creating a function for prediction

def diabetes_prediction(input_data):
    
    
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loadm.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'The person is not diabetic'
    else:
      return 'The person is diabetic'
  
    
def main():
      
    #title
    st.title('Diabetes Prediction Web App')
      
      
    # getting the input data from the user
      
    Pregnancies = st.text_input('Number of pregnancies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('Blood pressure readings')
    SkinThickness = st.text_input('The SkinThickness')
    Insulin = st.text_input('Insulin level')
    BMI = st.text_input('BMI Value')
    DiabetesPedigreeFunction = st.text_input('DiabetesPedigreeFunction Value')
    Age = st.text_input('Age of the person')
      
      
    # code for prediction
      
    diagnosis = ''
      
     # creating a button for prediction
      
    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
          

    st.success(diagnosis)
      
      
      
      
if __name__=='__main__':
    main()
      
      
      