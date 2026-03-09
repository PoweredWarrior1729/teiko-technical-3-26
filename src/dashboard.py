import streamlit as st
import pandas as pd
import numpy as np
import plotly
import plotly.express as px
import sqlite3
import plotly.graph_objects as go

st.title("Interactive Dashboard")

conn = sqlite3.connect("cell-count.db")
summary_table = pd.read_sql_query("SELECT * FROM Summary", conn)
conn.close()

st.subheader("Summary Table")

st.dataframe(summary_table)

st.subheader("Box Plot of Relative Frequencies of Cells in Responders and Nonreponders")

fig = plotly.io.read_json('assets/boxes.json')
st.plotly_chart(fig)
st.text("See Results section for analysis of these plots.")

st.subheader("All melanoma PBMC samples at baseline")

st.dataframe(pd.read_csv("assets/sample.csv"))

st.subheader("Requested Statistics about these Samples")

f = open("assets/requested_stats.txt", 'r')
st.text(f.read())
f.close()
