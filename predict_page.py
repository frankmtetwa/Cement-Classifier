# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 12:25:38 2023

@author: Frank Mtetwa
"""
import streamlit as st
import pickle
import numpy as np
import pandas as pd

def load_model():
    # open the saved pickle file
    with open('cement_optimized.pkl', 'rb') as f:
        km = pickle.load(f)
    return km

km = load_model()

def show_predict_page():
    st.title("Cement Quality Prediction")
    
    #st.write("""### We need some information to predict the stability""")
    
    Al2O3 = st.number_input("Enter Al2O3 (%)")
    CaO = st.number_input("Enter CaO (%)")
    Fe2O3 = st.number_input("Enter Fe2O3 (%)")
    MgO = st.number_input("Enter MgO (%)")
    SiO2 = st.number_input("Enter SiO2 (%)")
    
    ok = st.button('Predict')
    if ok:
        X  = np.array([[Al2O3,CaO,Fe2O3,MgO,SiO2]])
        
        # convert the Numpy array into a Pandas DataFrame
        X_df = pd.DataFrame(X,columns=['Al2O3 (%)','CaO (%)','Fe2O3 (%)','MgO (%)','SiO2 (%)'])
        
        # Predict Quality
        y_pred = km.predict(X_df)
        #st.subheader(f"The estimated quality is {y_pred}")
        if y_pred == 0:
            st.subheader("Okay")
        elif y_pred ==1:
            st.subheader("Bad")
        else:
            st.subheader("Good")
