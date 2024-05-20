import sqlite3
import os
import time
from contextlib import closing

# Database file paths
sql_file_path = 'File_Management/Database/wifi_saved_list.sql'
db_path = 'File_Management/Database/wifi_saved_list.db'

def execute_sql_file(sql_file_path, db_path):
    """
    Execute an SQL file to create and populate the SQLite database.
    """
    # Connect to the database (it will create the database file if it doesn't exist)
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        
        # Read the SQL file
        with open(sql_file_path, 'r') as sql_file:
            sql_script = sql_file.read()
        
        # Execute the SQL script
        cursor.executescript(sql_script)
        
        # Commit changes
        conn.commit()

def create_or_connect_db(db_path):
    retries = 5
    delay = 5
    while retries > 0:
        try:
            with closing(sqlite3.connect(db_path)) as conn:
                with closing(conn.cursor()) as cursor:
                    # Try to create the table to check if the database is valid
                    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS wifi_details (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        ssid TEXT,
                        security TEXT,
                        password TEXT
                    )
                    ''')
                    conn.commit()
            return sqlite3.connect(db_path)
        except sqlite3.DatabaseError as e:
            print(f"Database error: {e}")
            retries -= 1
            if retries > 0:
                print(f"Retrying in {delay} seconds...")
                time.sleep(delay)
    return None

# Check if the .db file exists, if not, convert .sql to .db
if not os.path.exists(db_path):
    print(f"{db_path} not found. Creating database from {sql_file_path}.")
    execute_sql_file(sql_file_path, db_path)

# Create or connect to the SQLite database
conn = create_or_connect_db(db_path)

def save_wifi_details(ssid, security, password):
    """
    Save Wi-Fi details to the database.

    Parameters:
    ssid (str): The SSID of the Wi-Fi network.
    security (str): The security type of the Wi-Fi network (e.g., WPA2, WPS).
    password (str): The password of the Wi-Fi network.
    """
    if conn:
        with closing(conn.cursor()) as cursor:
            # Check if the SSID and password already exist in the database
            cursor.execute('''
            SELECT * FROM wifi_details WHERE ssid = ? AND password = ?
            ''', (ssid, password))
            result = cursor.fetchone()
            
            if result:
                print(f"Wi-Fi details for SSID: {ssid} with the same password already exist. Skipping save.")
            else:
                cursor.execute('''
                INSERT INTO wifi_details (ssid, security, password)
                VALUES (?, ?, ?)
                ''', (ssid, security, password))
                conn.commit()
                print(f"Saved Wi-Fi details for SSID: {ssid}")

def get_all_wifi_details():
    """
    Retrieve all saved Wi-Fi details from the database.

    Returns:
    list of tuples: A list of all Wi-Fi details in the format (id, ssid, security, password).
    """
    if conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute('SELECT * FROM wifi_details')
            return cursor.fetchall()
    return []

def get_wifi_details_by_ssid(ssid):
    """
    Retrieve Wi-Fi details by SSID.

    Parameters:
    ssid (str): The SSID of the Wi-Fi network.

    Returns:
    tuple: The Wi-Fi details in the format (id, ssid, security, password).
    """
    if conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute('SELECT * FROM wifi_details WHERE ssid = ?', (ssid,))
            return cursor.fetchone()
    return None

# Example usage
if __name__ == '__main__':
    # Example Wi-Fi details
    ssid = 'ExampleNetwork'
    security = 'WPA2'
    password = 'password123'

    # Save the Wi-Fi details
    save_wifi_details(ssid, security, password)

    # Retrieve and print all saved Wi-Fi details
    wifi_details = get_all_wifi_details()
    for detail in wifi_details:
        print(f"ID: {detail[0]}, SSID: {detail[1]}, Security: {detail[2]}, Password: {detail[3]}")

    # Retrieve and print Wi-Fi details for a specific SSID
    specific_wifi_details = get_wifi_details_by_ssid(ssid)
    if specific_wifi_details:
        print(f"Retrieved Wi-Fi details for SSID {ssid}: Security: {specific_wifi_details[2]}, Password: {specific_wifi_details[3]}")
    else:
        print(f"No Wi-Fi details found for SSID: {ssid}")

# Close the database connection when done
if conn:
    conn.close()
