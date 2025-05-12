import pandas as pd
import streamlit as st

# Page setup
st.set_page_config(page_title="Streetmoney MLB HR Predictor", layout="wide")
st.title("Streetmoney MLB HR Predictor")
st.subheader("Top Home Run Picks for Today")

# Load your home run data
df = pd.read_csv('homeruns.csv')

# Show column names and data preview
st.write("Column names:", df.columns)
st.write("Preview of data:")
st.write(df.head())

# Dropdown to select team
teams = df['team_abbrev'].unique()
selected_team = st.selectbox('Select Team', sorted(teams))

# Optional: Player name search
player_search = st.text_input("Search for Player (optional)").strip().lower()

# Opponent filter (using 'team_abbrev' column for both teams)
if 'team_abbrev' in df.columns:
    opponents = df[df['team_abbrev'] != selected_team]['team_abbrev'].unique()
    selected_opp = st.selectbox('Filter by Opponent (optional)', ['All'] + sorted(opponents))
else:
    selected_opp = 'All'

# Apply filters
filtered_df = df[df['team_abbrev'] == selected_team].copy()

if player_search:
    filtered_df = filtered_df[filtered_df['player'].str.lower().str.contains(player_search)]

if selected_opp != 'All':
    filtered_df = filtered_df[filtered_df['team_abbrev'] == selected_opp]

# Format HR probability as percentage
if 'hr_probability' in filtered_df.columns:
    filtered_df['hr_probability'] = filtered_df['hr_probability'].apply(lambda x: f"{x:.0%}")

# Sort and show top 5 HR picks
if 'hr_probability' in filtered_df.columns:
    filtered_df = filtered_df.sort_values(by='hr_probability', ascending=False).head(5)

# Show filtered predictions
st.subheader(f"Top Home Run Predictions for {selected_team}")
st.dataframe(filtered_df)
