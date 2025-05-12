import pandas as pd
import streamlit as st

# Set up the page
st.set_page_config(page_title="Streetmoney MLB HR Predictor", layout="wide")
st.title("Streetmoney MLB HR Predictor")
st.subheader("Top Home Run Picks for Today")

# Load your batter data CSV from GitHub
df = pd.read_csv('your_batter_data.csv')  # Replace with your actual file name

# Show the data in a table
st.dataframe(df)
