import sqlite3
conn = sqlite3.connect("internship.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS interns (
    id INTEGER PRIMARY KEY,
    name TEXT,
    track TEXT,
    stipend INTEGER
)
""")
cursor.execute("DELETE FROM interns")
cursor.execute("INSERT INTO interns VALUES (1, 'Soma', 'Data Science', 7000)")
cursor.execute("INSERT INTO interns VALUES (2, 'Ravi', 'Web Dev', 5000)")
cursor.execute("INSERT INTO interns VALUES (3, 'Anu', 'Data Science', 6500)")
cursor.execute("INSERT INTO interns VALUES (4, 'John', 'Web Dev', 4500)")
cursor.execute("INSERT INTO interns VALUES (5, 'Neha', 'Data Science', 8000)")
conn.commit()
print("Filtered Interns (Data Science, stipend > 5000):")
cursor.execute("""
SELECT * FROM interns
WHERE track = 'Data Science' AND stipend > 5000
""")
for row in cursor.fetchall():
    print(row)
print("\nAverage stipend per track:")
cursor.execute("""
SELECT track, AVG(stipend)
FROM interns
GROUP BY track
""")
for row in cursor.fetchall():
    print(row)
print("\nNumber of interns per track:")
cursor.execute("""
SELECT track, COUNT(*)
FROM interns
GROUP BY track
""")
for row in cursor.fetchall():
    print(row)
conn.close()