import subprocess

"""
Controlling the font size system-wide in Linux can vary depending on the desktop environment 
(e.g., GNOME, KDE, etc.). Below, I'll provide an example of how to adjust the font size using gsettings for 
GNOME-based environments. This approach involves modifying the system's settings for the default font size.
"""

def get_current_font_size():
    """
    Get the current font size setting from GNOME.
    """
    try:
        result = subprocess.run(
            ['gsettings', 'get', 'org.gnome.desktop.interface', 'text-scaling-factor'],
            stdout=subprocess.PIPE, check=True, universal_newlines=True
        )
        return float(result.stdout.strip())
    except subprocess.CalledProcessError as e:
        print(f"Error getting current font size: {e}")
        return None

def set_font_size(factor):
    """
    Set the font size in GNOME.

    Parameters:
    factor (float): The scaling factor for the font size (e.g., 1.0, 1.5, 2.0).
    """
    try:
        subprocess.run(
            ['gsettings', 'set', 'org.gnome.desktop.interface', 'text-scaling-factor', str(factor)],
            check=True
        )
        print(f"Font size set to scaling factor: {factor}")
    except subprocess.CalledProcessError as e:
        print(f"Error setting font size: {e}")

if __name__ == "__main__":
    current_font_size = get_current_font_size()
    if current_font_size is not None:
        print(f"Current font size scaling factor: {current_font_size}")

        try:
            new_font_size = float(input("Enter new font size scaling factor (e.g., 1.0, 1.5, 2.0): "))
            set_font_size(new_font_size)
        except ValueError:
            print("Invalid input. Please enter a numerical value.")
    else:
        print("Unable to retrieve current font size.")
