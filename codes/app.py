import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

st.set_page_config(layout="wide")
cont = st.container(height=1000)

cont.write("""
    # Practice app to learn streamlit
""")

df = px.data.tips()
cont.table(df.head())

col1, col2 = cont.columns(2)

col1.write(f"## Total customers: {df.shape[0]}")
fig = px.sunburst(df, path=['sex', 'day', 'time'], values='total_bill', color='day')
col1.plotly_chart(fig)

x = st.sidebar.selectbox("Time", df['time'].unique())

with st.spinner(text="In progress"):
    
    fig = px.box(df[df['time'] == x], x='sex', y='tip')
    col2.plotly_chart(fig)

    fig = px.box(df[df['time'] == x], x='size', y='tip')
    col2.plotly_chart(fig)

    fig = px.scatter(df[df['time'] == x], x='total_bill', y='tip')
    col2.plotly_chart(fig)