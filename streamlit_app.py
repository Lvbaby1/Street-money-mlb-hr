import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Sample data (home run predictions)
data = {
    "Player": ["Aaron Judge", "Kyle Schwarber", "Shohei Ohtani", "Matt Olson", "Pete Alonso"],
    "Team": ["Yankees", "Phillies", "Dodgers", "Braves", "Mets"],
    "Opponent": ["Red Sox", "Marlins", "Giants", "Cubs", "Nationals"],
    "HR Probability": [0.42, 0.38, 0.35, 0.34, 0.33]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Set up Streamlit page configuration
st.set_page_config(page_title="Streetmoney MLB HR Predictor", layout="wide")
st.title("Streetmoney MLB HR Predictor")
st.subheader("Top Home Run Picks for Today")

# Display the predictions as a table
st.write("### Home Run Predictions")
st.dataframe(df.style.format({"HR Probability": "{:.0%}"}))

# Bar chart for HR probabilities
st.write("### HR Probability Visualization")
fig, ax = plt.subplots(figsize=(8, 4))
ax.bar(df["Player"], df["HR Probability"], color='skyblue')
ax.set_xlabel('Player')
ax.set_ylabel('HR Probability')
ax.set_title('Home Run Probabilities')
plt.xticks(rotation=45)
st.pyplot(fig)

# Add a button for user interaction (optional)
if st.button('Refresh Predictions'):
    st.write("Predictions have been refreshed!")
