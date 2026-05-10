import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

# Connect to the database
conn = sqlite3.connect('shiptivity.db')

# 1. Daily Active Users 
# We add 'unixepoch' so SQLite knows how to read the numbers
dau_query = """
SELECT 
    DATE(login_timestamp, 'unixepoch') as activity_date, 
    COUNT(DISTINCT user_id) as daily_active_users
FROM login_history
GROUP BY activity_date
ORDER BY activity_date ASC;
"""
dau_df = pd.read_sql_query(dau_query, conn)

# 2. Status Changes
status_query = """
SELECT 
    cardID, 
    COUNT(id) as total_changes
FROM card_change_history
GROUP BY cardID
ORDER BY total_changes DESC;
"""
status_df = pd.read_sql_query(status_query, conn)

conn.close()

# --- Generate Graphs ---

# Graph 1: DAU (Now with data!)
plt.figure(figsize=(12, 6))
plt.plot(pd.to_datetime(dau_df['activity_date']), dau_df['daily_active_users'], color='#1f77b4')
plt.title('Daily Active Users (DAU)')
plt.xlabel('Date')
plt.ylabel('Unique Users')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('dau_graph.png')

# Graph 2: Status Changes
plt.figure(figsize=(12, 6))
plt.bar(status_df['cardID'].astype(str), status_df['total_changes'], color='#2ca02c')
plt.title('Total Status Changes per Card')
plt.xlabel('Card ID')
plt.ylabel('Count of Changes')
# Hide X-axis labels if there are too many cards
plt.xticks([]) 
plt.tight_layout()
plt.savefig('status_changes_graph.png')

print("Success! Both graphs now contain data.")