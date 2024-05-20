import os
import sqlite3
from pywifi import PyWiFi, const

# Database file path
db_path = 'File_Management/Database/wifi_saved_list.db'

def connect_db(db_path):
    try:
        return sqlite3.connect(db_path)
    except sqlite3.DatabaseError as e:
        print(f"Database error: {e}")
        return None

# Connect to the SQLite database
conn = connect_db(db_path)

def remove_wifi_details(ssid):
    """
    Remove Wi-Fi details from the database.

    Parameters:
    ssid (str): The SSID of the Wi-Fi network to remove.
    """
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM wifi_details WHERE ssid = ?', (ssid,))
            conn.commit()
            print(f"Removed Wi-Fi details for SSID: {ssid}")
        except sqlite3.Error as e:
            print(f"Error removing Wi-Fi details: {e}")

def disconnect_from_wifi(ssid_to_disconnect):
    """
    Disconnect from a specific Wi-Fi network.

    Parameters:
    ssid_to_disconnect (str): The SSID of the Wi-Fi network to disconnect from.
    """
    wifi = PyWiFi()
    iface = wifi.interfaces()[0]
    networks = iface.scan_results()
    for network in networks:
        if network.ssid == ssid_to_disconnect:
            iface.disconnect()
            print(f"Disconnected from Wi-Fi network: {ssid_to_disconnect}")
            break
    else:
        print(f"Wi-Fi network {ssid_to_disconnect} not found or already disconnected")

if __name__ == '__main__':
    # SSID of the Wi-Fi network to remove and disconnect from
    ssid_to_remove = input("Enter the SSID of the Wi-Fi network to remove and disconnect from: ")

    # Remove Wi-Fi details from the database
    remove_wifi_details(ssid_to_remove)

    # Disconnect from the specified Wi-Fi network
    disconnect_from_wifi(ssid_to_remove)

# Close the database connection when done
if conn:
    conn.close()
