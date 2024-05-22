import os
from cryptography.fernet import Fernet
import getpass

# Define the directory path to save the encrypted password
directory_path = 'File_Management/config/security/pin'
os.makedirs(directory_path, exist_ok=True)

def get_encryption_key():
    """
    Retrieve the encryption key.
    This function should be replaced with the actual method to retrieve the key.
    """
    # For demonstration purposes, we use a hardcoded key
    # Replace this with secure key retrieval in a real application
    key = b'your-secure-encryption-key'  # Example key, ensure this is 32 bytes
    return key

def encrypt_password(password, key):
    """
    Encrypt the password using the provided key.

    Parameters:
    password (str): The password to be encrypted.
    key (bytes): The encryption key.

    Returns:
    bytes: The encrypted password.
    """
    cipher_suite = Fernet(key)
    encrypted_password = cipher_suite.encrypt(password.encode())
    return encrypted_password

def get_unique_filename(directory_path, base_name, extension):
    """
    Generate a unique filename in the given directory.
    If the base_name.extension already exists, append a number to the base_name.

    Parameters:
    directory_path (str): The path to the directory.
    base_name (str): The base name for the file.
    extension (str): The file extension.

    Returns:
    str: A unique filename.
    """
    file_path = os.path.join(directory_path, f"{base_name}{extension}")
    counter = 1
    while os.path.exists(file_path):
        file_path = os.path.join(directory_path, f"{base_name}{counter}{extension}")
        counter += 1
    return file_path

def save_encrypted_password(file_path, encrypted_password):
    """
    Save the encrypted password to a file.

    Parameters:
    file_path (str): The path to the file where the encrypted password will be saved.
    encrypted_password (bytes): The encrypted password.
    """
    try:
        with open(file_path, 'wb') as file:
            file.write(encrypted_password)
        print(f"Encrypted password saved to {file_path}")
    except Exception as e:
        print(f"Error saving encrypted password: {e}")

if __name__ == "__main__":
    # Ask for the input password
    password = getpass.getpass("Enter the password: ")

    # Get the encryption key
    key = get_encryption_key()

    # Encrypt the password
    encrypted_password = encrypt_password(password, key)

    # Ask for the input file name
    file_name = input("Enter the file name (without extension) or press Enter to use the default name 'password': ").strip()
    if not file_name:
        file_name = "password"

    # Get a unique filename if the default name is used or if the file already exists
    file_path = get_unique_filename(directory_path, file_name, ".encamdv")

    # Save the encrypted password to the file
    save_encrypted_password(file_path, encrypted_password)
