import pandas as pd
import streamlit as st

# Load batter data CSV
df = pd.read_csv('your_batter_data.csv')  # Replace with actual file name

# Display the data in a table
st.dataframe(df)
