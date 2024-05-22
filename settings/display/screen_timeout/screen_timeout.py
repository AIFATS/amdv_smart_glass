import subprocess

"""
Controlling the screen timeout on Linux systems typically involves interacting with system settings or using 
tools like xset for X11-based environments. Below is a Python script that sets the screen timeout based on user 
input, supporting values such as 15 seconds, 30 seconds, 1 minute, 2 minutes, 5 minutes, and 10 minutes.

sudo apt-get install x11-xserver-utils
"""

# Define the mapping of timeout values to seconds
timeout_mapping = {
    '15 seconds': 15,
    '30 seconds': 30,
    '1 minute': 60,
    '2 minutes': 120,
    '5 minutes': 300,
    '10 minutes': 600
}

def set_screen_timeout(timeout):
    """
    Set the screen timeout to the specified value.

    Parameters:
    timeout (str): The timeout duration as a string (e.g., '1 minute', '5 minutes').
    """
    if timeout not in timeout_mapping:
        print("Invalid timeout value. Please choose from the predefined values.")
        return

    timeout_seconds = timeout_mapping[timeout]

    # Command to set screen timeout using xset
    try:
        subprocess.run(['xset', 's', str(timeout_seconds)], check=True)
        print(f"Screen timeout set to {timeout}.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to set screen timeout: {e}")

if __name__ == "__main__":
    # List of valid timeout options
    options = list(timeout_mapping.keys())
    print("Choose a screen timeout duration:")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    # Get user input
    try:
        choice = int(input("Enter the number corresponding to your choice: "))
        if 1 <= choice <= len(options):
            set_screen_timeout(options[choice - 1])
        else:
            print("Invalid choice. Please run the script again and choose a valid option.")
    except ValueError:
        print("Invalid input. Please run the script again and enter a number.")
