import sqlite3
import pandas as pd

# Step 1: Connect to SQLite database
conn = sqlite3.connect("student_data.db")

# Step 2: Create cursor
cursor = conn.cursor()

# Step 3: Create students table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
""")

# Step 4: Create marks table
cursor.execute("""
CREATE TABLE IF NOT EXISTS marks (
    student_id INTEGER,
    subject TEXT,
    marks INTEGER
)
""")

# Step 5: Insert data into students table
cursor.execute("DELETE FROM students")  # clear old data
students_data = [
    (1, 'Ravi', 20),
    (2, 'Priya', 21),
    (3, 'Arjun', 19),
    (4, 'Sneha', 22)
]

cursor.executemany("INSERT INTO students VALUES (?, ?, ?)", students_data)

# Step 6: Insert data into marks table
cursor.execute("DELETE FROM marks")  # clear old data
marks_data = [
    (1, 'Math', 85),
    (2, 'Math', 90),
    (3, 'Math', 75),
    (4, 'Math', 95),
    (1, 'Science', 80),
    (2, 'Science', 88),
    (3, 'Science', 70),
    (4, 'Science', 92)
]

cursor.executemany("INSERT INTO marks VALUES (?, ?, ?)", marks_data)

conn.commit()

# ---------------------------
# SELECT Query
# ---------------------------
print("\nSELECT Query Result:")
cursor.execute("SELECT * FROM students")
for row in cursor.fetchall():
    print(row)

# ---------------------------
# WHERE Query
# ---------------------------
print("\nWHERE Query Result (marks > 85):")
cursor.execute("SELECT * FROM marks WHERE marks > 85")
for row in cursor.fetchall():
    print(row)

# ---------------------------
# GROUP BY Query
# ---------------------------
print("\nGROUP BY Query Result (Average marks per student):")
cursor.execute("""
SELECT student_id, AVG(marks)
FROM marks
GROUP BY student_id
""")
for row in cursor.fetchall():
    print(row)

# ---------------------------
# JOIN Query
# ---------------------------
print("\nJOIN Query Result:")
cursor.execute("""
SELECT students.name, marks.subject, marks.marks
FROM students
INNER JOIN marks
ON students.id = marks.student_id
""")
for row in cursor.fetchall():
    print(row)

# ---------------------------
# Load into Pandas (Data Science)
# ---------------------------
print("\nData loaded into Pandas DataFrame:")
query = """
SELECT students.name, marks.subject, marks.marks
FROM students
JOIN marks
ON students.id = marks.student_id
"""

df = pd.read_sql_query(query, conn)

print(df)

# Close connection
conn.close()
