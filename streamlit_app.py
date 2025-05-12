import streamlit as st
import pandas as pd

# Page setup
st.set_page_config(page_title="Streetmoney MLB HR Predictor", layout="wide")
st.title("Streetmoney MLB HR Predictor")
st.subheader("Top HR Hitters from MLB Savant Data")

# Load the updated CSV file with the correct name (exit_velocity 2.csv)
df = pd.read_csv("exit_velocity 2.csv")

# Show column names for debugging (if necessary)
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

# Optional: Filter out players with low expected HR (adjust as needed)
df = df[df["Expected HR"] >= 2]  # Example filter (can adjust this value)

# Sort by Expected HR (or other stat)
df = df.sort_values(by="Expected HR", ascending=False)

# Display the top 10 players
st.dataframe(df[["Player", "Team", "Exit Velo", "Launch Angle", "Barrel %", "xwOBA", "Expected HR"]].head(10))
