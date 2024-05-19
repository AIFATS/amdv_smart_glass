from components.clock.clock import read_config, get_time_in_timezone
from components.Screen_resolution.Screen_resolution import calculate_screen_size
from components.gps_coordinates.gps_coordinates import get_gps_coordinates
from components.get_weather.get_weather import get_weather
import tkinter as tk
from datetime import datetime
import pytz

# Function to update the time label
def update_time():
    current_time = get_time_in_timezone(time_zone).strftime('%Y-%m-%d %H:%M')
    time_label.config(text=current_time)
    root.after(1000, update_time)  # Update time every second

def update_weather():
    lat, lon = get_gps_coordinates()
    weather_info = get_weather(lat, lon)
    weather_label.config(text=weather_info)
    root.after(60000, update_weather)  # Update weather every 60 seconds

config_file_path = 'File_Management/config/.config'

# Read the configuration file
config = read_config(config_file_path)

# Get the time zone from the config file
time_zone = config.get('clock', 'UTC')

# Example values
throw_ratio = 1.5
distance = 0.75
aspect_ratio_width = 16
aspect_ratio_height = 9

# Calculate the screen size
width, height = calculate_screen_size(throw_ratio, distance, aspect_ratio_width, aspect_ratio_height)

pixels_per_meter = 3779.527559
screen_width_pixels = int(width * pixels_per_meter)
screen_height_pixels = int(height * pixels_per_meter)

# Create the main window
root = tk.Tk()

# Set the window to be transparent
root.attributes("-transparentcolor", "black")  # Set black as the transparent color
root.attributes("-alpha", 0.1)  # Set window transparency (0.0 = fully transparent, 1.0 = fully opaque)

# Set the geometry of the window
root.geometry(f"{screen_width_pixels}x{screen_height_pixels}")

# Create a label to display the time
time_label = tk.Label(root, font=("Helvetica", 24), fg="#000000")  # Dark background, black text
time_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Create a label to display the weather
weather_label = tk.Label(root, font=("Helvetica", 24), fg="#000000")  # Dark background, black text
weather_label.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

# Start the time update loop
update_time()

# Start the time and weather update loops
update_weather()

# Start the Tkinter event loop
root.mainloop()