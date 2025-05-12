import streamlit as st
import pandas as pd

# Load CSV
df = pd.read_csv("homeruns.csv")

# Clean up player names
df["player"] = df["player"].str.strip()

# Drop rows with missing xHR
df = df[df["xhr"].notnull()]

# Sort by expected home runs
df = df.sort_values(by="xhr", ascending=False)

# Set up Streamlit
st.set_page_config(page_title="Streetmoney MLB HR Predictor", layout="wide")
st.title("Streetmoney MLB HR Predictor")
st.subheader("Top Home Run Candidates (Based on xHR)")

# Show data
st.dataframe(df[["player", "team_abbrev", "xhr"]].reset_index(drop=True))
