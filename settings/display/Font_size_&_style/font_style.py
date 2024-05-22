import os
import re
from PIL import ImageFont
from IPython.display import display, HTML

# Define the directory path
directory_path = 'File_Management/config/Font_style'
text = "This is text"

def get_font_names(directory):
    font_names = set()
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.ttf') or file.endswith('.otf'):
                font_name_without_extension = os.path.splitext(file)[0]
                clean_font_name = re.sub(r'_\d+$', '', font_name_without_extension)
                font_names.add(clean_font_name)
    
    return font_names

def display_text_with_fonts(directory, text="This is text"):
    html_output = '<div style="display: flex; flex-wrap: wrap;">'
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.ttf') or file.endswith('.otf'):
                font_path = os.path.join(root, file)
                try:
                    font = ImageFont.truetype(font_path, 30)
                    font_name = os.path.splitext(file)[0]
                    clean_font_name = re.sub(r'_\d+$', '', font_name)
                    html_output += f'<div style="margin: 10px; font-family: {clean_font_name}; font-size: 24px;">{text}</div>'
                    html_output += f'<div style="margin: 10px; font-size: 16px;">Font Style: {clean_font_name}</div>'
                    html_output += '<hr>'
                except Exception as e:
                    print(f"Could not load font {file}: {e}")
    html_output += '</div>'
    return html_output

if __name__ == "__main__":
    # Get the font names without extension and suffixes
    font_names = get_font_names(directory_path)
    
    # Display the text with each font style
    html = display_text_with_fonts(directory_path, text)
    display(HTML(html))
