import sqlite3
import pandas as pd

conn = sqlite3.connect("cell-count.db")
sql_query = """SELECT * FROM Samples
WHERE sample_type = 'PBMC' AND time = 0 AND subject_id IN
(
    SELECT subject_id FROM Subjects WHERE treatment = 'miraclib'
    AND condition = 'melanoma'
)"""
pd.read_sql_query(sql_query, conn).to_csv("assets/sample.csv")

f = open('assets/requested_stats.txt', 'w')

sql_query = """SELECT * FROM Samples WHERE
sample_type = 'PBMC' AND time = 0 AND subject_id IN
(
    SELECT subject_id FROM Subjects WHERE
    treatment = 'miraclib' AND condition = 'melanoma' AND project = 'prj1'
)"""
print("Number of samples from prj1:",
    len(pd.read_sql_query(sql_query, conn)), file=f)

sql_query = """SELECT * FROM Samples WHERE
sample_type = 'PBMC' AND time = 0 AND subject_id IN
(
    SELECT subject_id FROM Subjects WHERE
    treatment = 'miraclib' AND condition = 'melanoma' AND project = 'prj2'
)"""
print("Number of samples from prj2:",
    len(pd.read_sql_query(sql_query, conn)), file=f)

sql_query = """SELECT * FROM Samples WHERE
sample_type = 'PBMC' AND time = 0 AND subject_id IN
(
    SELECT subject_id FROM Subjects WHERE
    treatment = 'miraclib' AND condition = 'melanoma' AND project = 'prj3'
)"""
print("Number of samples from prj3:",
    len(pd.read_sql_query(sql_query, conn)), file=f)

sql_query = """SELECT * FROM Samples WHERE
sample_type = 'PBMC' AND time = 0 AND subject_id IN
(
    SELECT subject_id FROM Subjects WHERE
    treatment = 'miraclib' AND condition = 'melanoma' AND response = 'yes'
)"""
print("Number of responders:",
    len(pd.read_sql_query(sql_query, conn)), file=f)

sql_query = """SELECT * FROM Samples WHERE
sample_type = 'PBMC' AND time = 0 AND subject_id IN 
(
    SELECT subject_id FROM Subjects WHERE
    treatment = 'miraclib' AND condition = 'melanoma' AND response = 'no'
)"""
print("Number of nonresponders:",
    len(pd.read_sql_query(sql_query, conn)), file=f)

sql_query = """SELECT * FROM Samples WHERE
sample_type = 'PBMC' AND time = 0 AND subject_id IN 
(
    SELECT subject_id FROM Subjects WHERE
    treatment = 'miraclib' AND condition = 'melanoma' AND sex = 'M'
)"""
print("Number of males:",
    len(pd.read_sql_query(sql_query, conn)), file=f)

sql_query = """SELECT * FROM Samples WHERE
sample_type = 'PBMC' AND time = 0 AND subject_id IN 
(
    SELECT subject_id FROM Subjects WHERE
    treatment = 'miraclib' AND condition = 'melanoma' AND sex = 'F'
)"""
print("Number of females:",
    len(pd.read_sql_query(sql_query, conn)), file=f)

sql_query = """SELECT pop_count FROM Summary WHERE
population = 'b_cell' AND sample_id IN 
(
    SELECT sample_id FROM Samples WHERE
    time = 0 AND subject_id IN
    (
        SELECT subject_id FROM Subjects WHERE
        sex = 'M' AND condition = 'melanoma'
    )
)"""
print("Average B cells in melanoma males at the beginning of treatment:",
    pd.read_sql_query(sql_query, conn)['pop_count'].mean(), "B cells", file=f)

conn.close()
