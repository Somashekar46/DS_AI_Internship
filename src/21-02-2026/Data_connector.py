import sqlite3
import pandas as pd
conn = sqlite3.connect("internship.db")
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS interns")
cursor.execute("DROP TABLE IF EXISTS mentors")
cursor.execute("""
CREATE TABLE interns (
    intern_id INTEGER PRIMARY KEY,
    intern_name TEXT,
    track TEXT,
    stipend INTEGER
)
""")
cursor.execute("""
CREATE TABLE mentors (
    mentor_id INTEGER PRIMARY KEY,
    mentor_name TEXT,
    track TEXT
)
""")
cursor.executemany("""
INSERT INTO interns VALUES (?, ?, ?, ?)
""", [
    (1, 'Soma', 'Data Science', 7000),
    (2, 'Ravi', 'Web Dev', 5000),
    (3, 'Anu', 'Data Science', 6500),
    (4, 'Neha', 'Web Dev', 5500),
    (5, 'Arjun', 'Data Science', 8000)
])
cursor.executemany("""
INSERT INTO mentors VALUES (?, ?, ?)
""", [
    (101, 'Dr. Sharma', 'Data Science'),
    (102, 'Ms. Priya', 'Web Dev')
])
conn.commit()
query = """
SELECT interns.intern_name, interns.track, mentors.mentor_name, interns.stipend
FROM interns
INNER JOIN mentors
ON interns.track = mentors.track
"""
df = pd.read_sql_query(query, conn)
print("\nInterns with their mentors:\n")
print(df)
conn.close()