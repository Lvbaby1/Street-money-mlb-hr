import streamlit as st
import pandas as pd

# Page setup
st.set_page_config(page_title="Streetmoney MLB HR Predictor", layout="wide")
st.title("Streetmoney MLB HR Predictor")
st.subheader("Top HR Hitters from MLB Savant Data")

# Load the first CSV file (homeruns.csv - contains Expected HR 'XHR')
df_hr = pd.read_csv("homeruns.csv")

# Load the second CSV file (exit_velocity 2.csv - contains exit velocity data)
df_ev = pd.read_csv("exit_velocity 2.csv")

# Show column names for debugging (optional)
# st.write(df_hr.columns)
# st.write(df_ev.columns)

# Clean and rename columns for clarity
df_hr = df_hr.rename(columns={
    "player_name": "Player", 
    "team_abbrev": "Team", 
    "XHR": "Expected HR"  # Rename 'XHR' to 'Expected HR'
})

df_ev = df_ev.rename(columns={
    "player_name": "Player",
    "exit_velocity": "Exit Velo",
    "launch_angle": "Launch Angle",
    "barrel_batted_rate": "Barrel %",
    "estimated_woba_using_speedangle": "xwOBA"
})

# Merge the two dataframes on the "Player" column (adjust if the identifier is different)
merged_df = pd.merge(df_hr, df_ev, on="Player", how="inner")

# Optional: Filter out players with low Expected HR (you can adjust this threshold)
merged_df = merged_df[merged_df["Expected HR"] >= 1]  # Example filter for Expected HR greater than or equal to 1

# Sort by Expected HR or another column if needed
merged_df = merged_df.sort_values(by="Expected HR", ascending=False)

# Display the merged data with relevant stats
st.dataframe(merged_df[["Player", "Team", "Exit Velo", "Launch Angle", "Barrel %", "xwOBA", "Expected HR"]].head(10))
