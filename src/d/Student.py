
import sqlite3

# connect to database
conn = sqlite3.connect("school.db")

# create cursor (used to execute SQL)
cursor = conn.cursor()

# create students table
cursor.execute("CREATE TABLE IF NOT EXISTS students(id INTEGER, name TEXT, subject TEXT, marks INTEGER)")

# create departments table
cursor.execute("CREATE TABLE IF NOT EXISTS departments(id INTEGER, dept TEXT)")

# insert data
cursor.execute("DELETE FROM students")

# To avoid duplicate data when running the script multiple times
cursor.execute("DELETE FROM departments")

cursor.execute("INSERT INTO students VALUES(1,'Soma','Math',85)")
cursor.execute("INSERT INTO students VALUES(2,'John','Science',92)")
cursor.execute("INSERT INTO students VALUES(3,'Alice','Math',78)")

cursor.execute("INSERT INTO departments VALUES(1,'Engineering')")
cursor.execute("INSERT INTO departments VALUES(2,'Medical')")
cursor.execute("INSERT INTO departments VALUES(3,'Engineering')")

# commit changes
conn.commit()

# SELECT
print("\nSELECT:")
for row in cursor.execute("SELECT * FROM students"):
    print(row)

print("\nSELECT:")
for row in cursor.execute("SELECT * FROM departments"):
    print(row)
    
# WHERE, Aggreate Functions
print("\nWHERE marks > 80:")
for row in cursor.execute("SELECT * FROM students WHERE marks > 80"):
    print(row)

# GROUP BY
print("\nGROUP BY subject:")
for row in cursor.execute("SELECT subject, AVG(marks) FROM students GROUP BY subject"):
    print(row)

# JOIN
print("\nJOIN students and departments:")
for row in cursor.execute("""
SELECT students.name, departments.dept
FROM students
JOIN departments
ON students.id = departments.id
"""):
    print(row)

# close connection
conn.close()
