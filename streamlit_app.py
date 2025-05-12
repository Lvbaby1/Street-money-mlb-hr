import pandas as pd
import streamlit as st

# Page setup
st.set_page_config(page_title="Streetmoney MLB HR Predictor", layout="wide")
st.title("Streetmoney MLB HR Predictor")
st.subheader("Top Home Run Picks for Today")

# Load your home run data
df = pd.read_csv('homeruns.csv')

# Show the first few rows to confirm it's loading correctly (optional)
st.write("Preview of data:")
st.write(df.head())

# Team filter using the correct column: 'team_abbrev'
teams = df['team_abbrev'].unique()
selected_team = st.selectbox('Select Team', sorted(teams))

# Filter data by selected team
filtered_df = df[df['team_abbrev'] == selected_team]

# Display filtered home run data
st.subheader(f"Home Run Predictions for {selected_team}")
st.dataframe(filtered_df)
