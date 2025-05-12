import pandas as pd
import streamlit as st

# Load your homeruns.csv file
df = pd.read_csv("homeruns.csv")

# Clean up player names and filter missing values
df["player"] = df["player"].str.strip()
df = df[df["xhr"].notnull()]
df = df.sort_values(by="xhr", ascending=False)

# Prediction logic based on expected home runs (xhr)
def predict_hr(xhr):
    if xhr > 0.4:
        return "High"
    elif xhr > 0.3:
        return "Medium"
    else:
        return "Low"

df["HR Prediction"] = df["xhr"].apply(predict_hr)

# Streamlit page setup
st.set_page_config(page_title="Streetmoney MLB HR Predictor", layout="wide")
st.title("Streetmoney MLB HR Predictor")
st.subheader("Top Home Run Picks Based on Expected HRs (xHR)")

# Optional: team filter
teams = df["team_abbrev"].dropna().unique()
selected_teams = st.multiselect("Filter by Team", sorted(teams))
if selected_teams:
    df = df[df["team_abbrev"].isin(selected_teams)]

# Show filtered and sorted dataframe with prediction
st.dataframe(
    df[["player", "team_abbrev", "xhr", "HR Prediction"]]
    .reset_index(drop=True)
    .rename(columns={"player": "Player", "team_abbrev": "Team", "xhr": "Expected HRs", "HR Prediction": "Prediction"})
)

# Optional: Show top 5 hitters with highest xHR
st.subheader("Top 5 Predicted HR Hitters")
st.dataframe(
    df[["player", "team_abbrev", "xhr", "HR Prediction"]]
    .sort_values(by="xhr", ascending=False)
    .head(5)
    .reset_index(drop=True)
    .rename(columns={"player": "Player", "team_abbrev": "Team", "xhr": "Expected HRs", "HR Prediction": "Prediction"})
)
