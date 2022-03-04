# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 20:30:51 2022

@author: Oluwasegun
"""
import numpy as np
import pickle

loadhm = pickle.load(open('C:/Users/Administrator/Documents/Data science P/Heart Disease App/trained_model.sav','rb'))

input_data = (57,1,2,150,168,0,1,174,0,1.6,2,0,2)

# changing the input_data to numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = loadhm.predict(input_data_reshaped)
print(prediction)

if (prediction[0] == 0):
  print('The person is free from heart disease')
else:
  print('The person is likely to develop heart disease')