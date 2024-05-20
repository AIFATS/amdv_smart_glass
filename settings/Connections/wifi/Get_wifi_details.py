import subprocess
import re
import qrcode
import sqlite3
import os
from pyzbar.pyzbar import decode
import getmac

# Database file path
db_path = 'File_Management/Database/wifi_saved_list.db'

def get_password_by_ssid(ssid):
    """
    Retrieve the password for a given SSID from the database.

    Parameters:
    ssid (str): The SSID of the Wi-Fi network.

    Returns:
    str: The password associated with the given SSID, or None if not found.
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('SELECT password FROM wifi_details WHERE ssid = ?', (ssid,))
    password = cursor.fetchone()
    conn.close()
    return password[0] if password else None


def get_connected_wifi_info():
    """
    Get information about the connected Wi-Fi interface.

    Returns:
    tuple: A tuple containing the SSID, MAC address, and IP address of the connected Wi-Fi interface.
    """
    try:
        # Run the system command to get the Wi-Fi interface information
        output = subprocess.check_output(['iwgetid'], universal_newlines=True)

        # Use regular expressions to find the SSID
        ssid_match = re.search(r'ESSID:"([^"]+)"', output)

        # Extract SSID
        ssid = ssid_match.group(1).strip() if ssid_match else None

        # Get MAC address
        mac_address = getmac.get_mac_address(interface="wlan0")

        # Get IP address
        ip_address = subprocess.check_output(['hostname', '-I'], universal_newlines=True).strip()

        return ssid, mac_address, ip_address
    except Exception as e:
        print(f"Error retrieving Wi-Fi information: {e}")
        return None, None, None

def generate_qr_code(data):
    """
    Generate a QR code from the provided data.

    Parameters:
    data (str): The data to be encoded in the QR code.

    Returns:
    qrcode.QRCode: The generated QR code object.
    """
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(data)
    return qr

def display_wifi_info():
    # Get connected Wi-Fi information
    ssid, mac_address, ip_address = get_connected_wifi_info()

    if ssid is None:
        print("No Wi-Fi connection found.")
        return

    # Get password for the specified Wi-Fi SSID from the database
    password = get_password_by_ssid(ssid)
    if password:
        # Generate QR code for the password
        qr = generate_qr_code(password)
        qr_code_image = qr.make_image(fill_color="black", back_color="white")
        qr_code_image.show()
    else:
        print(f"No password found for SSID: {ssid}")

    # Display Wi-Fi information
    print(f"SSID: {ssid}")
    print(f"MAC Address: {mac_address}")
    print(f"IP Address: {ip_address}")

if __name__ == "__main__":
    display_wifi_info()
