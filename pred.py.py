# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 16:15:09 2024

@author: M S Mathai
"""

import streamlit as st
import pandas as pd
import numpy as np
import datetime
import xgboost as xgb


import joblib
date_time=datetime.datetime.now()
model=xgb.XGBRFRegressor()
model.load_model('xgb_model.json')

def main():
    html_temp="""
     <div style = "background-color:Green ">
     <h2 style="color:white;text-align:center;"> Car Price Prediction </h2>
     </div>
    """
   
    st.markdown(html_temp,unsafe_allow_html=True)
    st.write('')
    
    Present_Price = st.number_input('CURRENT PRICE (In Lakhs)',2.5,25.0,step=1.0)
    
    Kms_Driven =st.number_input('KILOMETERD DRIVEN',100,50000000,step=100)
    
    ft=st.selectbox('FUEL TYPE ',('Petrol','Diesel', 'CNG'))
    
    if ft =='PETROL':
        Fuel_Type=0
    elif ft=='DIESEL':
        Fuel_Type=1
    else:
        Fuel_Type=3
    
    St=st.selectbox('SELLER_TYPE ',('Dealer','Individual'))
    
    if St =='Dealer':
        Seller_Type=0
    elif St=='Individual':
        Seller_Type=1
    
    tt=st.selectbox(' TRANSMISSION_TYPE ',('Manual','Automatic'))
    if tt =='Manual':
        Transmission=0
    elif tt=='Automatic':
        Transmission=1
   
    Owner= st.number_input('OWNER',0,3,step=1)
    
    yr= st.number_input("YEARS",1990,date_time.year,step=1)
    Years=date_time.year-yr
    
    new_data=pd.DataFrame({
    'Present_Price':Present_Price,
    'Kms_Driven':Kms_Driven,
    'Fuel_Type':Fuel_Type,
    'Seller_Type':Seller_Type,
    'Transmission':Transmission,
    'Owner':Owner,
    'Years':Years
},index=[0])
    try: 
        if st.button('Predict'):
            prediction = model.predict(new_data)
            if prediction>0:
                st.balloons()
                st.success('You can sell the car for {:.2f} lakhs'.format(prediction[0]))
            else:
                st.warning("You will be not able to sell this car !!")
    except:
        st.warning("Opps!! Something went wrong\nTry again")
    
 

if __name__ == '__main__':
    main()