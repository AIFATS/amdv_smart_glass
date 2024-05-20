import subprocess

def set_airplane_mode(state):
    """
    Toggle airplane mode on or off.

    Parameters:
    state (bool): True to enable airplane mode, False to disable it.

    Returns:
    bool: True if the operation was successful, False otherwise.
    """
    try:
        if state:
            subprocess.check_call(["nmcli", "radio", "all", "off"])
        else:
            subprocess.check_call(["nmcli", "radio", "all", "on"])
        return True
    except subprocess.CalledProcessError as e:
        print(f"Failed to change airplane mode: {e}")
        return False

# Example usage:
airplane_mode = True  # Set to False to disable airplane mode
if set_airplane_mode(airplane_mode):
    print(f"Airplane mode {'enabled' if airplane_mode else 'disabled'} successfully.")
else:
    print("Failed to toggle airplane mode.")
