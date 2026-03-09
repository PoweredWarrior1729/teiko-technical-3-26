import sqlite3
import pandas as pd
import plotly.graph_objects as go

conn = sqlite3.connect("cell-count.db")

sql_query = "SELECT * FROM Summary WHERE sample_id IN (SELECT sample_id FROM Samples WHERE sample_type = 'PBMC' AND subject_id IN (SELECT subject_id FROM Subjects WHERE condition = 'melanoma' AND treatment = 'miraclib' AND response = 'yes'))"
yes_df = pd.read_sql_query(sql_query, conn)

sql_query = "SELECT * FROM Summary WHERE sample_id IN (SELECT sample_id FROM Samples WHERE sample_type = 'PBMC' AND subject_id IN (SELECT subject_id FROM Subjects WHERE condition = 'melanoma' AND treatment = 'miraclib' AND response = 'no'))"
no_df = pd.read_sql_query(sql_query, conn)

fig = go.Figure()

fig.add_trace(go.Box(

    y=yes_df['percentage'],
    x=yes_df['population'],
    name='Portion of cells in responders',
    marker_color='green'
))

fig.add_trace(go.Box(

    y=no_df['percentage'],
    x=no_df['population'],
    name='Portion of cells in nonresponders',
    marker_color='red'
))

fig.update_layout(boxmode='group')

fig.write_json("assets/boxes.json")
