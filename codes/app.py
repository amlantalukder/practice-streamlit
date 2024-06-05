import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.write("""
    # Practice app to learn streamlit (Updated)
""")

df = sns.load_dataset("titanic")
df
x = st.sidebar.selectbox("Passenger Class", df['class'].unique())

with st.spinner(text="In progress"):
    fig, ax = plt.subplots(figsize=(10, 4))
    ax = sns.boxplot(df[df['class'] == x], x='sex', y='age')
    st.pyplot(fig)

