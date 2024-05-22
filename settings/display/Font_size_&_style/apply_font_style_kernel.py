import subprocess

"""
Make sure to replace "set_font" with the appropriate command for your system to apply the font style to the 
kernel. This could involve using tools provided by your operating system or desktop environment. Additionally, 
ensure that the font_style line in the .config file follows the format font_style="path_to_font_file".
"""

# Path to the .config file
config_file_path = 'File_Management/config/.config'

def apply_font_style_to_kernel(font_file_path):
    # Example command to apply font style to kernel (replace with actual command for your system)
    command = f"set_font {font_file_path}"

    try:
        # Execute the command
        subprocess.run(command, shell=True, check=True)
        print("Font style applied to kernel successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error applying font style to kernel: {e}")

# Read the font style from the .config file
def read_font_style_from_config():
    try:
        with open(config_file_path, 'r') as f:
            for line in f:
                if line.startswith('font_style='):
                    return line.strip().split('=')[1].strip('"')
    except FileNotFoundError:
        print(f"Config file '{config_file_path}' not found.")
    except Exception as e:
        print(f"Error reading font style from config: {e}")

if __name__ == "__main__":
    # Read the font style from the .config file
    font_file_path = read_font_style_from_config()

    if font_file_path:
        # Apply the font style to the kernel
        apply_font_style_to_kernel(font_file_path)
