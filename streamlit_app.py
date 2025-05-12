import streamlit as st
import pandas as pd

# Page setup
st.set_page_config(page_title="Streetmoney MLB HR Predictor", layout="wide")
st.title("Streetmoney MLB HR Predictor")
st.subheader("Top HR Hitters from MLB Savant Data")

# Load the updated CSV file
df = pd.read_csv("exit_velocity_2.csv")

# Show column names for debugging
# st.write(df.columns)

# Clean and filter data
df = df.rename(columns={
    "player_name": "Player",
    "exit_velocity": "Exit Velo",
    "launch_angle": "Launch Angle",
    "barrel_batted_rate": "Barrel %",
    "team_abbrev": "Team",
    "estimated_woba_using_speedangle": "xwOBA",
    "xHR": "Expected HR"
})

# Optional: Filter out players with low expected HR
df = df[df["Expected HR"] >= 2]  # Example filter (you can adjust as needed)

# Sort by Expected HR or Barrel %
df = df.sort_values(by="Expected HR", ascending=False)

# Display the top 10 players
st.dataframe(df[["Player", "Team", "Exit Velo", "Launch Angle", "Barrel %", "xwOBA", "Expected HR"]].head(10))
