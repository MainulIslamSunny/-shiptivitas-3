import sqlite3
conn = sqlite3.connect('shiptivity.db')
cursor = conn.cursor()

# Check how many rows are in the login table
cursor.execute("SELECT COUNT(*) FROM login_history")
count = cursor.fetchone()[0]
print(f"Total rows in login_history: {count}")

# Show the first 3 rows to check the column names and data format
cursor.execute("SELECT * FROM login_history LIMIT 3")
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()