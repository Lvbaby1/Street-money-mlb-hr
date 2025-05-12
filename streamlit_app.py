import streamlit as st
import pandas as pd

st.set_page_config(page_title="Streetmoney Game Winner Predictor", layout="wide")
st.title("MLB Game Winner Predictor")
st.subheader("Simple model using ERA and batting average")

# Sample data for today’s games
data = {
    "Team_1": ["Yankees", "Dodgers", "Braves"],
    "Team_2": ["Red Sox", "Giants", "Cubs"],
    "Team_1_SP_ERA": [3.45, 2.95, 4.10],
    "Team_2_SP_ERA": [4.22, 3.80, 4.55],
    "Team_1_Bullpen_ERA": [3.98, 3.50, 4.20],
    "Team_2_Bullpen_ERA": [4.12, 3.90, 4.60],
    "Team_1_BA": [0.251, 0.267, 0.245],
    "Team_2_BA": [0.243, 0.258, 0.238]
}

df = pd.DataFrame(data)

# Prediction logic
def predict_winner(row):
    team_1_score = (1 / row['Team_1_SP_ERA']) + (1 / row['Team_1_Bullpen_ERA']) + row['Team_1_BA']
    team_2_score = (1 / row['Team_2_SP_ERA']) + (1 / row['Team_2_Bullpen_ERA']) + row['Team_2_BA']
    return row['Team_1'] if team_1_score > team_2_score else row['Team_2']

df["Predicted_Winner"] = df.apply(predict_winner, axis=1)

# Show the table
st.dataframe(df)
