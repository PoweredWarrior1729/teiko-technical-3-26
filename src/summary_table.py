import sqlite3
import pandas as pd

conn = sqlite3.connect("cell-count.db")
cursor = conn.cursor()
df = pd.read_csv('assets/cell-count.csv')

summary_text = "INSERT INTO Summary (sample_id, total_count, population, "
summary_text += "pop_count, percentage) VALUES (?, ?, ?, ?, ?)"
summary_list = [0,0,"",0,0]

populations = ("b_cell", "cd8_t_cell", "cd4_t_cell", "nk_cell", "monocyte")

for index, row in df.iterrows():
    summary_list[0] = int(row.iloc[7][6:])
    summary_list[1] = 0
    for i in range(10,15):
        summary_list[1] += row.iloc[i]
    for i in range(5):
        summary_list[2] = populations[i]
        summary_list[3] = row.iloc[i+10]
        summary_list[4] = summary_list[3] / summary_list[1]
        cursor.execute(summary_text, summary_list)

conn.commit()
conn.close()
