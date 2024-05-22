import os
from cryptography.fernet import Fernet
import getpass

# Define the directory path where the encrypted passwords are stored
directory_path = 'File_Management/config/security/pin'

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

def check_password_in_files(encrypted_password, directory_path):
    """
    Check if the encrypted password matches any of the encrypted password files in the directory.

    Parameters:
    encrypted_password (bytes): The encrypted password to check.
    directory_path (str): The path to the directory containing the encrypted password files.

    Returns:
    bool: True if a match is found, False otherwise.
    """
    for file_name in os.listdir(directory_path):
        file_path = os.path.join(directory_path, file_name)
        if os.path.isfile(file_path):
            try:
                with open(file_path, 'rb') as file:
                    stored_encrypted_password = file.read()
                    if stored_encrypted_password == encrypted_password:
                        return True
            except Exception as e:
                print(f"Error reading file {file_name}: {e}")
    return False

if __name__ == "__main__":
    # Ask for the input password
    password = getpass.getpass("Enter the password: ")

    # Get the encryption key
    key = get_encryption_key()

    # Encrypt the input password
    encrypted_password = encrypt_password(password, key)

    # Check if the encrypted password matches any stored encrypted passwords
    if check_password_in_files(encrypted_password, directory_path):
        print("Success: Password matched!")
    else:
        print("Failure: Password did not match.")
