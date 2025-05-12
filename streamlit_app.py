import pandas as pd
import streamlit as st

# Set up the page
st.set_page_config(page_title="Streetmoney MLB HR Predictor", layout="wide")
st.title("Streetmoney MLB HR Predictor")
st.subheader("Top Home Run Picks for Today")

# Load the batter data CSV from GitHub
df = pd.read_csv('homeruns.csv')  # Correct file name

# Filter by team (if 'Team' is a column in the data)
teams = df['Team'].unique()
selected_team = st.selectbox('Select Team', teams)

# Filter the dataframe based on the selected team
filtered_df = df[df['Team'] == selected_team]

# Display the filtered data in a table
st.dataframe(filtered_df)
