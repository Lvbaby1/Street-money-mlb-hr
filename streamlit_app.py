import pandas as pd
import streamlit as st

# Page setup
st.set_page_config(page_title="Streetmoney MLB HR Predictor", layout="wide")
st.title("Streetmoney MLB HR Predictor")
st.subheader("Top Home Run Picks for Today")

# Load your home run data
df = pd.read_csv('homeruns.csv')

# Show preview of raw data (optional)
st.write("Preview of data:")
st.write(df.head())

# Team filter using 'team_abbrev'
teams = df['team_abbrev'].unique()
selected_team = st.selectbox('Select Team', sorted(teams))

# Filter the DataFrame after team is selected
filtered_df = df[df['team_abbrev'] == selected_team].copy()

# Optional: Format home run probability column (if it exists)
if 'hr_probability' in filtered_df.columns:
    filtered_df['hr_probability'] = filtered_df['hr_probability'].apply(lambda x: f"{x:.0%}")

# Display results
st.subheader(f"Home Run Predictions for {selected_team}")
st.dataframe(filtered_df)
