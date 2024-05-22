import os

"""
run this sudo apt-get install xbacklight
for brightness
control the brightness
"""

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

def change_brightness(step):
    """
    Change the display brightness by the specified step.

    Parameters:
    step (int): The step to change the brightness by (positive to increase, negative to decrease).
    """
    brightness_path = get_brightness_path()
    max_brightness_path = get_max_brightness_path()

    with open(max_brightness_path, 'r') as f:
        max_brightness = int(f.read().strip())

    with open(brightness_path, 'r') as f:
        current_brightness = int(f.read().strip())

    new_brightness = current_brightness + int((step / 100) * max_brightness)
    new_brightness = max(0, min(max_brightness, new_brightness))

    with open(brightness_path, 'w') as f:
        f.write(str(new_brightness))
    print(f"Brightness changed by {step}%. New brightness is {int((new_brightness / max_brightness) * 100)}%")

if __name__ == "__main__":
    while True:
        action = input("Enter action (set, change, exit): ").strip().lower()
        if action == "set":
            level = int(input("Enter brightness level (0-100): ").strip())
            set_brightness(level)
        elif action == "change":
            step = int(input("Enter brightness step (positive to increase, negative to decrease): ").strip())
            change_brightness(step)
        elif action == "exit":
            break
        else:
            print("Invalid action. Please enter 'set', 'change', or 'exit'.")
