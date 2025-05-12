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

# Clean and rename columns for clarity (using exact names as typed)
df_hr = df_hr.rename(columns={
    "player_name": "Player",  # Ensure 'Player' matches
    "team_abbrev": "Team", 
    "XHR": "Expected HR"  # Rename 'XHR' to 'Expected HR'
})

df_ev = df_ev.rename(columns={
    "max_hit_speed": "Exit Velo",        # Update 'max_hit_speed' to 'Exit Velo'
    "avg_hit_angle": "Launch Angle",     # Update 'avg_hit_angle' to 'Launch Angle'
    "barrel_batted_rate": "Barrel %",    # Keeping 'Barrel %' for barrel batted rate
    "estimated_woba_using_speedangle": "xwOBA"  # Rename xwOBA column
})

# Merge the two dataframes based on Player name (directly)
merged_df = pd.merge(df_hr, df_ev, on="Player", how="inner")

# Optional: Filter out players with low Expected HR (you can adjust this threshold)
merged_df = merged_df[merged_df["Expected HR"] >= 1]  # Example filter for Expected HR greater than or equal to 1

# Sort by Expected HR or another column if needed
merged_df = merged_df.sort_values(by="Expected HR", ascending=False)

# Display the merged data with relevant stats
st.dataframe(merged_df[["Player", "Team", "Exit Velo", "Launch Angle", "Barrel %", "xwOBA", "Expected HR"]].head(10))
