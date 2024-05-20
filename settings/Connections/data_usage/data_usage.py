import os
import sqlite3
import psutil
from datetime import datetime, timedelta

# Database file path
db_path = 'File_Management/config/Data_usage/data_usage.sql'

# Ensure the directory exists
os.makedirs(os.path.dirname(db_path), exist_ok=True)

# Create or connect to the SQLite database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create the table to store data usage
cursor.execute('''
CREATE TABLE IF NOT EXISTS data_usage (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    app_name TEXT,
    date TEXT,
    data_used REAL,
    monthly_data REAL
)
''')
conn.commit()

# Initialize previous data usage counters
prev_sent = psutil.net_io_counters().bytes_sent
prev_recv = psutil.net_io_counters().bytes_recv

def get_network_usage():
    """
    Get system-wide network usage.
    """
    global prev_sent, prev_recv
    counters = psutil.net_io_counters()
    sent = counters.bytes_sent - prev_sent
    recv = counters.bytes_recv - prev_recv
    prev_sent = counters.bytes_sent
    prev_recv = counters.bytes_recv
    return sent + recv

def save_data_usage():
    today = datetime.now().date().isoformat()
    data_used = get_network_usage()

    # For simplicity, assume all data usage is for a single app called 'System'
    cursor.execute('''
    INSERT INTO data_usage (app_name, date, data_used)
    VALUES (?, ?, ?)
    ''', ('System', today, data_used))
    
    conn.commit()

def calculate_monthly_usage():
    """
    Calculate and update the monthly data usage.
    """
    first_day_of_month = datetime.now().replace(day=1).date()
    last_day_of_last_month = first_day_of_month - timedelta(days=1)
    first_day_of_last_month = last_day_of_last_month.replace(day=1)

    cursor.execute('''
    SELECT app_name, AVG(data_used) as avg_daily_data
    FROM data_usage
    WHERE date BETWEEN ? AND ?
    GROUP BY app_name
    ''', (first_day_of_last_month.isoformat(), last_day_of_last_month.isoformat()))

    for row in cursor.fetchall():
        app_name, avg_daily_data = row
        cursor.execute('''
        UPDATE data_usage
        SET monthly_data = ?
        WHERE app_name = ? AND date = ?
        ''', (avg_daily_data, app_name, last_day_of_last_month.isoformat()))
    
    conn.commit()

if __name__ == '__main__':
    # Save data usage daily
    save_data_usage()

    # Check if the month has changed and calculate monthly usage
    today = datetime.now().date()
    if today.day == 1:
        calculate_monthly_usage()

# Close the database connection when done
conn.close()
