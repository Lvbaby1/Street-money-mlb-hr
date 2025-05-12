import pandas as pd
import streamlit as st

# Load the batter data CSV
df = pd.read_csv('homeruns.csv')

# Display the column names to check for the correct one
st.write(df.columns)
