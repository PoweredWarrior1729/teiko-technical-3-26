def main():
    import sqlite3
    import pandas as pd
    conn = sqlite3.connect("cell-count.db")
    cursor = conn.cursor()

    cursor.execute("""
CREATE TABLE IF NOT EXISTS Subjects (
    subject_id INTEGER PRIMARY KEY,
    project TEXT NOT NULL,
    condition TEXT NOT NULL,
    age INTEGER,
    sex TEXT NOT NULL,
    treatment TEXT NOT NULL,
    response TEXT
)
""")

    cursor.execute("""
CREATE TABLE IF NOT EXISTS Samples (
    sample_id INTEGER PRIMARY KEY,
    subject_id INTEGER,
    sample_type TEXT NOT NULL,
    time INTEGER,
    b_cell INTEGER,
    cd8_t_cell INTEGER,
    cd4_t_cell INTEGER,
    nk_cell INTEGER,
    monocyte INTEGER,
    FOREIGN KEY (subject_id) REFERENCES Subjects(subject_id)
)
""")

    cursor.execute("""
CREATE TABLE IF NOT EXISTS Summary (
    data_id INTEGER PRIMARY KEY AUTOINCREMENT,
    sample_id INTEGER,
    total_count INTEGER,
    population TEXT NOT NULL,
    pop_count INTEGER,
    percentage REAL,
    FOREIGN KEY (sample_id) REFERENCES Samples(sample_id)
)
""")

    df = pd.read_csv('assets/cell-count.csv')

    subject_text = "INSERT INTO Subjects (subject_id, project, condition, age, "
    subject_text += "sex, treatment, response) VALUES (?, ?, ?, ?, ?, ?, ?)"
    subject_list = [0, 1, "", 0, "", "", ""]

    samples_text = "INSERT INTO Samples (sample_id, subject_id, sample_type, time, "
    samples_text += "b_cell, cd8_t_cell, cd4_t_cell, nk_cell, monocyte) "
    samples_text += "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
    samples_list = [0, 0, "", 0, 0, 0, 0, 0, 0]

    for index, row in df.iterrows():
        if index % 3 == 0:
            subject_list[0] = int(row.iloc[1][3:])
            subject_list[1] = row.iloc[0]
            subject_list[2:7] = row.iloc[2:7]
            cursor.execute(subject_text, subject_list)
        samples_list[0] = int(row.iloc[7][6:])
        samples_list[1] = int(row.iloc[1][3:])
        samples_list[2:9] = row.iloc[8:15]
        cursor.execute(samples_text, samples_list)

    conn.commit()
    conn.close()
    print("Loading complete.")
