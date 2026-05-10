import sqlite3

# Connect to the database
conn = sqlite3.connect('shiptivity.db')
cursor = conn.cursor()

# Read the dump file
with open('shiptivity.dump', 'r') as f:
    sql_script = f.read()

# Execute the script to fill the database
try:
    cursor.executescript(sql_script)
    conn.commit()
    print("Data imported successfully!")
except Exception as e:
    print(f"An error occurred: {e}")

conn.close()