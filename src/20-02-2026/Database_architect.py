import sqlite3

# Connect to SQLite database (creates internship.db if not exists)
conn = sqlite3.connect("internship.db")

# Create cursor
cursor = conn.cursor()

# Create interns table
cursor.execute("""
CREATE TABLE IF NOT EXISTS interns (
    id INTEGER PRIMARY KEY,
    name TEXT,
    track TEXT,
    stipend INTEGER
)
""")

# Insert sample data
cursor.execute("INSERT INTO interns VALUES (1, 'Soma', 'Data Science', 15000)")
cursor.execute("INSERT INTO interns VALUES (2, 'Rahul', 'Web Dev', 12000)")
cursor.execute("INSERT INTO interns VALUES (3, 'Anita', 'Data Science', 18000)")
cursor.execute("INSERT INTO interns VALUES (4, 'Vikram', 'Web Dev', 14000)")
cursor.execute("INSERT INTO interns VALUES (5, 'Neha', 'AI/ML', 20000)")

# Save changes
conn.commit()

# SELECT only name and track
cursor.execute("SELECT name, track FROM interns")

# Fetch and display results
rows = cursor.fetchall()

print("Intern Name and Track:")
for row in rows:
    print(row)

# Close connection
conn.close()