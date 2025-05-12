import streamlit as st
import pandas as pd

st.set_page_config(page_title="Streetmoney MLB HR Predictor", layout="wide")
st.title("Streetmoney MLB HR Predictor")
st.subheader("Top Home Run Picks for Today")

# Load your CSV
df = pd.read_csv("homeruns.csv")

# Clean column names
df.columns = df.columns.str.strip()

# Ensure HR Probability is numeric
df["HR Probability"] = pd.to_numeric(df["HR Probability"], errors="coerce")

# --- STEP 1: Filter by HR Probability using a slider ---
min_hr_prob = st.slider("Minimum HR Probability", 0.0, 1.0, 0.3)
filtered_df = df[df["HR Probability"] >= min_hr_prob]

# --- STEP 3: Sort the table by HR Probability (high to low) ---
filtered_df = filtered_df.sort_values(by="HR Probability", ascending=False)

# --- STEP 2: Bar Chart using Streamlit ---
st.subheader("Bar Chart: HR Probabilities")
chart_data = filtered_df[["Player", "HR Probability"]].set_index("Player")
st.bar_chart(chart_data)

# --- Display the table ---
st.subheader("Filtered Predictions Table")
st.dataframe(filtered_df.style.format({"HR Probability": "{:.0%}"}))
