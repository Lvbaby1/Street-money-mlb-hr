import streamlit as st
import pandas as pd

st.set_page_config(page_title="Streetmoney MLB HR Predictor", layout="wide")
st.title("Streetmoney MLB HR Predictor")
st.subheader("Top Home Run Picks for Today")

# Example HR prediction data
data = {
    "Player": ["Aaron Judge", "Kyle Schwarber", "Shohei Ohtani", "Matt Olson", "Pete Alonso"],
    "Team": ["Yankees", "Phillies", "Dodgers", "Braves", "Mets"],
    "Opponent": ["Red Sox", "Marlins", "Giants", "Cubs", "Nationals"],
    "HR Probability": [0.42, 0.38, 0.35, 0.34, 0.33]
}

df = pd.DataFrame(data)

# Display table
st.dataframe(df.style.format({"HR Probability": "{:.0%}"}))
