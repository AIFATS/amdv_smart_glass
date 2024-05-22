import os
from datetime import datetime
import pytz

"""
get clock time with config
"""

def read_config(file_path):
    config = {}
    with open(file_path, 'r') as file:
        for line in file:
            if '=' in line:
                key, value = line.strip().split('=', 1)
                config[key] = value
    return config

def get_time_in_timezone(time_zone_str):
    # Get the current time in the specified time zone
    tz = pytz.timezone(time_zone_str)
    current_time = datetime.now(tz)
    return current_time

# Specify the path to the .config file
config_file_path = 'File_Management/config/.config'

# Read the configuration file
config = read_config(config_file_path)

# Get the time zone from the config file
time_zone = config.get('clock', 'UTC')

# Get the current time in the specified time zone
current_time = get_time_in_timezone(time_zone)

# Print the current time
print(f"The current time in {time_zone} is: {current_time.strftime('%Y-%m-%d %H:%M:%S')}")