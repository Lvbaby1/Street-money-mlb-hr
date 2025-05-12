import streamlit as st
import pandas as pd

# Load your homeruns.csv file
df = pd.read_csv("homeruns.csv")

# Basic cleanup
df["player"] = df["player"].str.strip()
df = df[df["xhr"].notnull()]
df = df.sort_values(by="xhr", ascending=False)

# Streamlit page setup
st.set_page_config(page_title="Streetmoney MLB HR Predictor", layout="wide")
st.title("Streetmoney MLB HR Predictor")
st.subheader("Top Home Run Picks Based on Expected HRs (xHR)")

# Optional: team filter
teams = df["team_abbrev"].dropna().unique()
selected_teams = st.multiselect("Filter by Team", sorted(teams))
if selected_teams:
    df = df[df["team_abbrev"].isin(selected_teams)]

# Show top results
st.dataframe(df[["player", "team_abbrev", "xhr"]].reset_index(drop=True).rename(
    columns={"player": "Player", "team_abbrev": "Team", "xhr": "Expected HRs"}
))
