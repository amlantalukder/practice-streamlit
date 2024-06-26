import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

df = px.data.tips()

st.set_page_config(layout="wide")

def figUpdateLayout(fig):
    base_font_size = 12
    fig.update_layout(title_font_size = base_font_size*2)
    fig.update_yaxes(title_font_size = base_font_size*1.5, tickfont_size = base_font_size*1.5)
    fig.update_xaxes(title_font_size = base_font_size*1.5, tickfont_size = base_font_size*1.5)
    return fig

with st.container(border=True):

    st.write("""
        # Practice app to learn streamlit
    """)

    st.table(df.head())

with st.container(height=1000):

    col1, col2 = st.columns(2)

    col1.write(f"## Total customers: {df.shape[0]}")
    fig = px.sunburst(df, path=['sex', 'day', 'time'], values='total_bill', color='day', width=800, height=600)
    col1.plotly_chart(fig, use_container_width=True)

    d = st.sidebar.selectbox("Day", df['day'].unique())
    p = st.sidebar.selectbox("Time", df['time'].unique())


    with st.spinner(text="In progress"):
        
        df_sub = df[(df['time'] == p) & (df['day'] == d)]

        fig = px.violin(df_sub, box=True, x='sex', y='tip', title="Tip amount based on gender")
        fig = figUpdateLayout(fig)
        col1.plotly_chart(fig, use_container_width=True)

        fig = px.box(df_sub, x='size', y='tip', title="Tip amount based on party size")
        fig = figUpdateLayout(fig)
        col2.plotly_chart(fig, use_container_width=True)

        fig = px.scatter(df_sub, x='total_bill', y='tip', title="Tip amount based on total bill")
        fig = figUpdateLayout(fig)
        col2.plotly_chart(fig, use_container_width=True)