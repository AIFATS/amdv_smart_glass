import subprocess

"""
control the volume level
system volume 
 Mute the system volume
 Unmute the system volume
"""

def set_volume(volume):
    """
    Set the system volume to the specified level.

    Parameters:
    volume (int): The volume level to set (0-100).
    """
    try:
        subprocess.run(['pactl', 'set-sink-volume', '@DEFAULT_SINK@', f'{volume}%'], check=True)
        print(f"Volume set to {volume}%")
    except subprocess.CalledProcessError as e:
        print(f"Error setting volume: {e}")

def change_volume(step):
    """
    Change the system volume by the specified step.

    Parameters:
    step (int): The step to change the volume by (positive to increase, negative to decrease).
    """
    if step > 0:
        try:
            subprocess.run(['pactl', 'set-sink-volume', '@DEFAULT_SINK@', f'+{step}%'], check=True)
            print(f"Volume increased by {step}%")
        except subprocess.CalledProcessError as e:
            print(f"Error increasing volume: {e}")
    else:
        try:
            subprocess.run(['pactl', 'set-sink-volume', '@DEFAULT_SINK@', f'{step}%'], check=True)
            print(f"Volume decreased by {step}%")
        except subprocess.CalledProcessError as e:
            print(f"Error decreasing volume: {e}")

def mute():
    """
    Mute the system volume.
    """
    try:
        subprocess.run(['pactl', 'set-sink-mute', '@DEFAULT_SINK@', '1'], check=True)
        print("Volume muted")
    except subprocess.CalledProcessError as e:
        print(f"Error muting volume: {e}")

def unmute():
    """
    Unmute the system volume.
    """
    try:
        subprocess.run(['pactl', 'set-sink-mute', '@DEFAULT_SINK@', '0'], check=True)
        print("Volume unmuted")
    except subprocess.CalledProcessError as e:
        print(f"Error unmuting volume: {e}")

if __name__ == "__main__":
    while True:
        action = input("Enter action (set, change, mute, unmute, exit): ").strip().lower()
        if action == "set":
            volume = int(input("Enter volume level (0-100): ").strip())
            set_volume(volume)
        elif action == "change":
            step = int(input("Enter volume step (positive to increase, negative to decrease): ").strip())
            change_volume(step)
        elif action == "mute":
            mute()
        elif action == "unmute":
            unmute()
        elif action == "exit":
            break
        else:
            print("Invalid action. Please enter 'set', 'change', 'mute', 'unmute', or 'exit'.")