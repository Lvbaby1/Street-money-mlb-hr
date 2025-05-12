import pandas as pd
import streamlit as st

# Sample data (home run predictions)
data = {
    "Player": ["Aaron Judge", "Kyle Schwarber", "Shohei Ohtani", "Matt Olson", "Pete Alonso"],
    "Team": ["Yankees", "Phillies", "Dodgers", "Braves", "Mets"],
    "Opponent": ["Red Sox", "Marlins", "Giants", "Cubs", "Nationals"],
    "HR Probability": [0.42, 0.38, 0.35, 0.34, 0.33]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Set up Streamlit page configuration
st.set_page_config(page_title="Streetmoney MLB HR Predictor", layout="wide")
st.title("Streetmoney MLB HR Predictor")
st.subheader("Top Home Run Picks for Today")

# Add filters for user interaction
team_filter = st.selectbox("Select Team", options=["All"] + list(df["Team"].unique()))
player_filter = st.selectbox("Select Player", options=["All"] + list(df["Player"].unique()))
opponent_filter = st.selectbox("Select Opponent", options=["All"] + list(df["Opponent"].unique()))

# Filter data based on user input
filtered_df = df
if team_filter != "All":
    filtered_df = filtered_df[filtered_df["Team"] == team_filter]
if player_filter != "All":
    filtered_df = filtered_df[filtered_df["Player"] == player_filter]
if opponent_filter != "All":
    filtered_df = filtered_df[filtered_df["Opponent"] == opponent_filter]

# Display filtered data as a table
st.write("### Home Run Predictions (Filtered)")
st.dataframe(filtered_df.style.format({"HR Probability": "{:.0%}"}))

# Add a button for user interaction (optional)
if st.button('Refresh Predictions'):
    st.write("Predictions have been refreshed!")
