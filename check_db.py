# import sqlite3

# conn = sqlite3.connect('shiptivity.db')
# cursor = conn.cursor()

# # Get the names of all tables in the database
# cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
# tables = cursor.fetchall()

# print("Tables found in database:")
# for table in tables:
#     print(f"- {table[0]}")

# conn.close()


import sqlite3

conn = sqlite3.connect('shiptivity.db')
cursor = conn.cursor()

print("Columns in 'card_change_history':")
cursor.execute("PRAGMA table_info(card_change_history);")
columns = cursor.fetchall()
for col in columns:
    print(f"- {col[1]}") # col[1] is the column name

conn.close()