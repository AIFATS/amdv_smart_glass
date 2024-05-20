import os

# Define the directory path
directory_path = 'File_Management/config/Ringtone_&_notification/ringtones'

def list_ogg_files(directory_path):
    # List all files in the directory
    all_files = os.listdir(directory_path)
    
    # Filter files with the .ogg extension
    ogg_files = [file.split('.')[0] for file in all_files if file.endswith('.ogg')]
    
    return ogg_files

# Get the list of .ogg file names
ogg_file_names = list_ogg_files(directory_path)

# Print the file names
for file_name in ogg_file_names:
    print(file_name)
