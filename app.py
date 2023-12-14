import pandas as pd
import numpy as np 
import streamlit as staticmethod

def load_data():
    return pd.read_csv('data/processed/bikes_completed.csv')

df = load_data()

st.dataframe(df)

if __name__ == '__main__':
    main()