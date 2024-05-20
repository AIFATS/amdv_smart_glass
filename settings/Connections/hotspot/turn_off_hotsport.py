import subprocess

# Path to the configuration file
config_path = 'File_Management/config/.config'

def read_config(config_path):
    config = {}
    with open(config_path, 'r') as file:
        for line in file:
            name, value = line.strip().split('=')
            config[name] = value
    return config

def turn_off_hotspot():
    try:
        # Turn off the hotspot
        subprocess.run(['nmcli', 'con', 'down', 'Hotspot'], check=True)
        print("Hotspot turned off successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to turn off hotspot: {e}")

if __name__ == "__main__":
    
    # Optionally, you can turn off the hotspot after some operations
    turn_off_hotspot()
