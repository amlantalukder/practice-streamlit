import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.write("""
    # Practice app to learn streamlit
""")

df = sns.load_dataset("titanic")
df
x = st.sidebar.selectbox("Passenger Class", df['class'].unique())

fig, ax = plt.subplots(figsize=(10, 4))
ax = sns.boxplot(df[df['class'] == x], x='sex', y='age')
st.pyplot(fig)

