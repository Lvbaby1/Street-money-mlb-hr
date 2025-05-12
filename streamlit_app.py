import pandas as pd
import streamlit as st

# Load the batter data CSV from GitHub
df = pd.read_csv('homeruns.csv')  # Correct file name

# Display the column names to check for the correct one
st.write(df.columns)  # This shows the column names
