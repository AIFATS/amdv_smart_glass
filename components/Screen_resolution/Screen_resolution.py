def calculate_screen_size(throw_ratio, distance, aspect_ratio_width, aspect_ratio_height):
    # Calculate the width of the projected image
    image_width = distance / throw_ratio
    
    # Calculate the height of the projected image using the aspect ratio
    image_height = (image_width * aspect_ratio_height) / aspect_ratio_width
    
    return image_width, image_height

# Example values
throw_ratio = 1.5  # Throw ratio of the projector
distance = 0.75  # Distance from projector to glass in meters
aspect_ratio_width = 16  # Aspect ratio width
aspect_ratio_height = 9  # Aspect ratio height

# Calculate the screen size
width, height = calculate_screen_size(throw_ratio, distance, aspect_ratio_width, aspect_ratio_height)

print(f"Screen width: {width:.2f} meters")
print(f"Screen height: {height:.2f} meters")

# If you also want the resolution in pixels and you know the pixels per meter
pixels_per_meter = 3779.527559  # example value for pixels per meter
screen_width_pixels = width * pixels_per_meter
screen_height_pixels = height * pixels_per_meter

print(f"Screen width: {screen_width_pixels:.0f} pixels")
print(f"Screen height: {screen_height_pixels:.0f} pixels")
