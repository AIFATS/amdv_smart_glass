import subprocess

"""
turn on the hotspot
"""

# Path to the configuration file
config_path = 'File_Management/config/.config'

def read_config(config_path):
    config = {}
    with open(config_path, 'r') as file:
        for line in file:
            name, value = line.strip().split('=')
            config[name] = value
    return config

def turn_on_hotspot(config_path):
    config = read_config(config_path)
    ssid = config.get('hotspot_ssid')
    password = config.get('hotspot_password')
    
    try:
        # Set up the hotspot
        subprocess.run([
            'nmcli', 'dev', 'wifi', 'hotspot', 'ifname', 'wlan0', 'con-name', 'Hotspot', 'ssid', ssid, 'band', 'bg', 'password', password
        ], check=True)
        print("Hotspot turned on successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to turn on hotspot: {e}")


if __name__ == "__main__":
    # Turn on the hotspot
    turn_on_hotspot(config_path)
    
    # Optionally, you can turn off the hotspot after some operations
    # turn_off_hotspot()
