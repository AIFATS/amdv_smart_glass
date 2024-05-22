import os
import time
from datetime import datetime

def get_brightness_path():
    """
    Get the path to the brightness control file.

    Returns:
    str: The path to the brightness control file.
    """
    backlight_path = '/sys/class/backlight/'
    for d in os.listdir(backlight_path):
        if 'intel_backlight' in d or 'acpi_video' in d:
            return os.path.join(backlight_path, d, 'brightness')
    raise FileNotFoundError("No backlight interface found.")

def get_max_brightness_path():
    """
    Get the path to the max brightness file.

    Returns:
    str: The path to the max brightness file.
    """
    backlight_path = '/sys/class/backlight/'
    for d in os.listdir(backlight_path):
        if 'intel_backlight' in d or 'acpi_video' in d:
            return os.path.join(backlight_path, d, 'max_brightness')
    raise FileNotFoundError("No backlight interface found.")

def set_brightness(level):
    """
    Set the display brightness to the specified level.

    Parameters:
    level (int): The brightness level to set (0-100).
    """
    brightness_path = get_brightness_path()
    max_brightness_path = get_max_brightness_path()

    with open(max_brightness_path, 'r') as f:
        max_brightness = int(f.read().strip())

    brightness_value = int((level / 100) * max_brightness)

    with open(brightness_path, 'w') as f:
        f.write(str(brightness_value))
    print(f"Brightness set to {level}%")

def auto_adjust_brightness():
    """
    Adjust the display brightness based on the time of day.
    """
    now = datetime.now().time()
    
    # Define brightness levels for different times of day
    morning_start = datetime.strptime("06:00", "%H:%M").time()
    day_start = datetime.strptime("08:00", "%H:%M").time()
    evening_start = datetime.strptime("18:00", "%H:%M").time()
    night_start = datetime.strptime("20:00", "%H:%M").time()

    if morning_start <= now < day_start:
        # Early morning brightness
        set_brightness(30)
    elif day_start <= now < evening_start:
        # Daytime brightness
        set_brightness(80)
    elif evening_start <= now < night_start:
        # Evening brightness
        set_brightness(50)
    else:
        # Night brightness
        set_brightness(20)

if __name__ == "__main__":
    try:
        while True:
            auto_adjust_brightness()
            time.sleep(60 * 10)  # Adjust every 10 minutes
    except KeyboardInterrupt:
        print("Auto-adjust brightness stopped.")
