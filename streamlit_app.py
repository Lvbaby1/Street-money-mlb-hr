import streamlit as st
import pandas as pd

# Load the CSV
df = pd.read_csv("exit_velocity 2.csv")

# Strip whitespace from name column
df["last_name, first_name"] = df["last_name, first_name"].str.strip()

# Filter for meaningful Exit Velocity data
df = df[df["max_hit_speed"].notnull()]
df = df[df["max_hit_speed"] >= 90]

# Set up Streamlit page
st.set_page_config(page_title="Streetmoney Exit Velo Leaders", layout="wide")
st.title("Streetmoney MLB Exit Velocity Leaders")
st.subheader("Statcast Power Metrics (From exit_velocity 2.csv)")

# Display filtered table
st.dataframe(
    df[["last_name, first_name", "max_hit_speed", "avg_hit_angle", "barrel_batted_rate", "estimated_woba_using_speedangle"]]
    .rename(columns={
        "last_name, first_name": "Player",
        "max_hit_speed": "Exit Velocity",
        "avg_hit_angle": "Launch Angle",
        "barrel_batted_rate": "Barrel %",
        "estimated_woba_using_speedangle": "xwOBA"
    })
    .sort_values(by="Exit Velocity", ascending=False)
    .reset_index(drop=True)
)
