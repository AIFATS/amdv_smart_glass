import os
from fprint import DiscoverDevices, EnrollFinger, init, deinit
from cryptography.fernet import Fernet

"""
To check for existing encrypted fingerprint data and ensure that a new scan is not stored if the fingerprint already exists, we need to:

Load the encryption key for existing fingerprints.
Decrypt and compare the new fingerprint scan against existing ones.
Stop scanning and send a success message if a match is found.
"""

# Initialize the fprint library
init()

# Discover fingerprint devices
devices = DiscoverDevices()
if not devices:
    print("No fingerprint devices found.")
    exit(1)

device = devices[0]
device.Open()

def get_encryption_key():
    """
    Retrieve the encryption key.
    This function should be replaced with the actual method to retrieve the key.
    """
    # For demonstration purposes, we use a hardcoded key
    # Replace this with secure key retrieval in a real application
    key = b'your-secure-encryption-key'  # Example key
    return key

def scan_and_save_fingerprint(device, file_path, directory_path):
    try:
        # Enroll fingerprint
        print("Please scan your finger...")
        enrolled_print = device.EnrollFinger()
        print("Fingerprint scanned successfully.")

        # Serialize the fingerprint data
        fingerprint_data = enrolled_print.data

        # Get the encryption key
        key = get_encryption_key()
        cipher_suite = Fernet(key)

        # Encrypt the fingerprint data
        encrypted_data = cipher_suite.encrypt(fingerprint_data)

        # Check if the encrypted fingerprint already exists
        for file_name in os.listdir(directory_path):
            if file_name.endswith('.encamdv'):
                with open(os.path.join(directory_path, file_name), 'rb') as file:
                    existing_encrypted_data = file.read()
                    if encrypted_data == existing_encrypted_data:
                        print("Fingerprint already exists. Stopping the scan.")
                        return

        # Save the encrypted fingerprint data to a file
        with open(file_path, 'wb') as file:
            file.write(encrypted_data)
        print(f"Encrypted fingerprint saved to {file_path}")

    except Exception as e:
        print(f"Error during fingerprint scanning: {e}")

    finally:
        device.Close()

def get_unique_filename(directory_path, base_name, extension):
    """
    Generate a unique filename in the given directory.
    If the base_name.extension already exists, append a number to the base_name.
    """
    file_path = os.path.join(directory_path, f"{base_name}{extension}")
    counter = 1
    while os.path.exists(file_path):
        file_path = os.path.join(directory_path, f"{base_name}{counter}{extension}")
        counter += 1
    return file_path

if __name__ == "__main__":
    # Define the directory path to save the encrypted fingerprint
    directory_path = 'File_Management/config/security/fingerprint'
    os.makedirs(directory_path, exist_ok=True)

    # Ask for the input file name
    file_name = input("Enter the file name (without extension) or press Enter to use the default name 'fingerprint': ").strip()
    if not file_name:
        file_name = "fingerprint"

    # Get a unique filename if the default name is used or if the file already exists
    file_path = get_unique_filename(directory_path, file_name, ".encamdv")

    # Scan the fingerprint and save the encrypted file
    scan_and_save_fingerprint(device, file_path, directory_path)

    # De-initialize the fprint library
    deinit()
