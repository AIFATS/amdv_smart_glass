import os
import sqlite3
import time
from contextlib import closing
from pywifi import PyWiFi, const, Profile
import pywifi

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

def get_all_wifi_details():
    """
    Retrieve all saved Wi-Fi details from the database.

    Returns:
    list of tuples: A list of all Wi-Fi details in the format (id, ssid, security, password).
    """
    if conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute('SELECT ssid, password FROM wifi_details')
            return cursor.fetchall()
    return []

def scan_available_wifi():
    """
    Scan and return available Wi-Fi networks.
    
    Returns:
    list of dicts: A list of available Wi-Fi networks with SSID and security type.
    """
    wifi = PyWiFi()
    iface = wifi.interfaces()[0]
    iface.scan()
    time.sleep(5)  # wait for scan to complete
    scan_results = iface.scan_results()

    available_networks = []
    for network in scan_results:
        ssid = network.ssid
        security = 'WPA/WPA2' if network.akm[0] == const.AKM_TYPE_WPA2PSK else 'WEP' if network.akm[0] == const.AKM_TYPE_WEP else 'OPEN'
        available_networks.append({'ssid': ssid, 'security': security})
    
    return available_networks

def connect_to_wifi(ssid, password):
    """
    Connect to a Wi-Fi network.

    Parameters:
    ssid (str): The SSID of the Wi-Fi network.
    password (str): The password of the Wi-Fi network.
    """
    wifi = PyWiFi()
    iface = wifi.interfaces()[0]

    # Disconnect from the current network
    iface.disconnect()
    time.sleep(2)

    # Create a new profile
    profile = Profile()
    profile.ssid = ssid
    profile.auth = const.AUTH_ALG_OPEN
    profile.akm.append(const.AKM_TYPE_WPA2PSK)
    profile.cipher = const.CIPHER_TYPE_CCMP
    profile.key = password

    iface.remove_all_network_profiles()
    tmp_profile = iface.add_network_profile(profile)
    iface.connect(tmp_profile)
    time.sleep(10)

    if iface.status() == const.IFACE_CONNECTED:
        print(f"Successfully connected to {ssid}")
    else:
        print(f"Failed to connect to {ssid}")

if __name__ == '__main__':
    # Get saved Wi-Fi details from the database
    saved_wifi_details = get_all_wifi_details()

    # Scan for available Wi-Fi networks
    available_networks = scan_available_wifi()

    # Compare and connect to a matching Wi-Fi network
    for saved_wifi in saved_wifi_details:
        for available_network in available_networks:
            if saved_wifi[0] == available_network['ssid']:
                print(f"Matching Wi-Fi network found: SSID={saved_wifi[0]}")
                connect_to_wifi(saved_wifi[0], saved_wifi[1])
                break

# Close the database connection when done
if conn:
    conn.close()
