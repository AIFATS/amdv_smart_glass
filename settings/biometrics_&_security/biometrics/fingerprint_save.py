import os
from fprint import DiscoverDevices, EnrollFinger, init, deinit
from cryptography.fernet import Fernet

"""
Creating a complete and functional biometric fingerprint scanning solution that connects to the kernel involves 
several steps. I'll provide a general framework for the code, but note that specifics can vary based on the 
fingerprint scanner hardware, drivers, and the libraries you're using.

We'll use the libfprint library, which is commonly used for fingerprint scanning on Linux systems. The libfprint
library provides functionality for fingerprint scanning and image processing. You will need to install libfprint
and its Python bindings (python-fprint).

Install libfprint and python-fprint
sudo apt-get install libfprint-dev
sudo apt-get install python3-fprint

Install additional dependencies
sudo apt-get install libusb-1.0-0-dev
sudo apt-get install libnss3-dev

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

def scan_and_save_fingerprint(device, file_path):
    try:
        # Enroll fingerprint
        print("Please scan your finger...")
        enrolled_print = device.EnrollFinger()
        print("Fingerprint scanned successfully.")

        # Serialize the fingerprint data
        fingerprint_data = enrolled_print.data

        # Generate a key for encryption
        key = Fernet.generate_key()
        cipher_suite = Fernet(key)

        # Encrypt the fingerprint data
        encrypted_data = cipher_suite.encrypt(fingerprint_data)

        # Save the encrypted fingerprint data to a file
        with open(file_path, 'wb') as file:
            file.write(encrypted_data)

        # Save the encryption key securely (for demonstration purposes, we print it here)
        # In a real application, you should store the key securely, e.g., in a hardware security module
        print(f"Encryption key: {key.decode()}")

    except Exception as e:
        print(f"Error during fingerprint scanning: {e}")

    finally:
        device.Close()

if __name__ == "__main__":
    # Define the directory path to save the encrypted fingerprint
    directory_path = 'File_Management/config/security/fingerprint'
    os.makedirs(directory_path, exist_ok=True)

    # Ask for the input file name
    file_name = input("Enter the file name (without extension) or press Enter to use the default name 'fingerprint': ").strip()
    if not file_name:
        file_name = "fingerprint"

    # Check if the input name already exists in the directory
    existing_files = [f for f in os.listdir(directory_path) if f.startswith(file_name) and f.endswith('.encamdv')]
    if existing_files:
        print(f"Error: A file with the name '{file_name}' already exists.")
        exit(1)

    # Get a unique filename if the default name is used or if the file already exists
    file_path = get_unique_filename(directory_path, file_name, ".encamdv")

    # Scan the fingerprint and save the encrypted file
    scan_and_save_fingerprint(device, file_path)

    # De-initialize the fprint library
    deinit()