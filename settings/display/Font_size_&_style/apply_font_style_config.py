import os

"""
his code takes the font name as input, constructs the font file path, updates the font_style line in the .config
 file with the new font file path, and then writes the updated content back to the .config file. Finally, it 
 prints a message indicating that the font style has been updated.
"""

# Define the .config file path
config_file = 'File_Management/config/.config'

def update_font_style(font_name):
    # Construct the font file path
    font_file_path = f'File_Management/config/Font_style/{font_name}/{font_name}_0.ttf'

    # Check if the font file exists
    if os.path.exists(font_file_path):
        try:
            # Open the .config file and update the font style
            with open(config_file, 'r') as f:
                lines = f.readlines()
            
            # Find and update the font style line
            for i, line in enumerate(lines):
                if line.startswith('font_style='):
                    lines[i] = f'font_style="{font_file_path}"\n'
                    break
            
            # Write the updated lines back to the .config file
            with open(config_file, 'w') as f:
                f.writelines(lines)

            print(f"Font style updated to: {font_file_path}")
        except Exception as e:
            print(f"Error updating font style: {e}")
    else:
        print(f"Font file not found: {font_file_path}")

if __name__ == "__main__":
    # Take input for the font name
    font_name = input("Enter the font name: ")

    # Update the font style in the .config file
    update_font_style(font_name)
