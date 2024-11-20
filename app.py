import streamlit as st
import joblib
import pandas as pd

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
    
    st.text(f"pred{prezzo(df_auto)}")
    
if __name__ == "__main__":
    main()  