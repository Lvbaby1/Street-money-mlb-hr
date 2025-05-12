import pandas as pd
import streamlit as st

# Page setup
st.set_page_config(page_title="Streetmoney MLB HR Predictor", layout="wide")
st.title("Streetmoney MLB HR Predictor")
st.subheader("Top Home Run Picks for Today")

# Load your home run data
df = pd.read_csv('homeruns.csv')

# Show preview (optional)
st.write("Preview of data:")
st.write(df.head())

# Team filter using 'team_abbrev'
teams = df['team_abbrev'].unique()
selected_team = st.selectbox('Select Team', sorted(teams))

# Optional: Player search within the selected team
player_search = st.text_input("Search for Player (optional)").strip().lower()

# Filter the DataFrame by selected team
filtered_df = df[df['team_abbrev'] == selected_team].copy()

# Further filter by player name if input is given
if player_search:
    filtered_df = filtered_df[filtered_df['player'].str.lower().str.contains(player_search)]

# Optional: Format home run probability column (if it exists)
if 'hr_probability' in filtered_df.columns:
    filtered_df['hr_probability'] = filtered_df['hr_probability'].apply(lambda x: f"{x:.0%}")

# Sort and show top 5 hitters by HR probability
if 'hr_probability' in filtered_df.columns:
    filtered_df = filtered_df.sort_values(by='hr_probability', ascending=False).head(5)

# Display results
st.subheader(f"Top Home Run Predictions for {selected_team}")
st.dataframe(filtered_df)
