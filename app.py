import streamlit as st
import joblib
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import Ridge

loaded = joblib.load('y_pred_Price')

brand = st.text_input("inserisci il brand")
kms_driven = st.text_input("inserisci i km")
fuel_type = st.text_input("inserisci l alimentaz")
old_year = st.text_input("inserisci l età del veicolo")

auto = {'brand':[brand],
        'kms_driven':[kms_driven],
        'fuel_type':[fuel_type],
        'old_year': [old_year],
        }

df_auto =pd.DataFrame(auto)

def prezzo(auto):
    pred = loaded.predict(df_auto)[0]
    
    return pred

def main():
    
    st.text(f"il valore dell'auto è: {int(prezzo(df_auto))}")
    
if __name__ == "__main__":
    main()  