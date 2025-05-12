import pandas as pd
import streamlit as st

# Set up the page
st.set_page_config(page_title="Streetmoney MLB HR Predictor", layout="wide")
st.title("Streetmoney MLB HR Predictor")
st.subheader("Top Home Run Picks for Today")

# Load the batter data CSV from GitHub
df = pd.read_csv('homeruns.csv')  # Use the file name you provided

# Display the data in a table
st.dataframe(df)
