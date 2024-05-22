import os

"""
update the ringtones in config file
"""

# Define the directory path
directory_path = 'File_Management/config/Ringtone_&_notification/ringtones'
config_file = 'File_Management/config/.config'

def update_audio_path(file_name):
    # Add .ogg extension if not present
    if not file_name.endswith('.ogg'):
        file_name += '.ogg'

    # Construct the full file path
    file_path = os.path.join(directory_path, file_name)

    try:
        # Read the contents of the .config file
        with open(config_file, 'r') as f:
            config_lines = f.readlines()

        # Check if call_ringtones entry exists
        for i, line in enumerate(config_lines):
            if line.startswith('call_ringtones='):
                # Update the existing path
                config_lines[i] = f'call_ringtones={file_path}\n'
                print(f"Updated audio file path: {file_path}")
                break
        else:
            # Add new entry
            config_lines.append(f'call_ringtones={file_path}\n')
            print(f"Added new audio file path: {file_path}")

        # Write the updated contents back to the .config file
        with open(config_file, 'w') as f:
            f.writelines(config_lines)

    except Exception as e:
        print(f"Error updating audio file path: {e}")

if __name__ == "__main__":
    # Take input for the file name
    file_name = input("Enter the file name (without extension): ")
    
    # Update or add the audio file path in the .config file
    update_audio_path(file_name)
