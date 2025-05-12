import streamlit as st
import pandas as pd

# Load the HR data
df = pd.read_csv("homeruns.csv")

# Strip extra spaces and clean names
df["player"] = df["player"].str.strip()

# Sort by expected home runs (xHR)
df = df[df["xhr"].notnull()]
df = df.sort_values(by="xhr", ascending=False)

# Streamlit layout
st.set_page_config(page_title="Streetmoney HR Picks", layout="wide")
st.title("Streetmoney MLB HR Predictor")
st.subheader("Top Power Hitters Based on xHR")

# Show data
st.dataframe(df[["player", "team_abbrev", "xhr", "pa", "avg_launch_speed", "avg_launch_angle", "brl_pa"]].reset_index(drop=True))
