import tkinter as tk
import psutil

"""
get wifi symbol on wallpaper
"""

def get_wifi_strength():
    """
    Fetches the Wi-Fi signal strength using psutil.
    Returns:
        int: Wi-Fi signal strength as a percentage, or None if not available.
    """
    try:
        interfaces = psutil.net_if_stats()
        wifi_interface = None
        for interface, stats in interfaces.items():
            if stats.isup and stats.speed > 0 and "wifi" in interface.lower():
                wifi_interface = interface
                break
        if wifi_interface:
            wifi_info = psutil.net_if_addrs()[wifi_interface]
            for info in wifi_info:
                if info.family == psutil.AF_LINK:
                    wifi_strength = info.attrs["signal_strength"]
                    return wifi_strength
    except Exception as e:
        print(f"Error getting Wi-Fi strength: {e}")
    return None

def draw_wifi_icon(canvas, strength):
    """
    Draws the Wi-Fi icon based on the signal strength.
    Args:
        canvas (tk.Canvas): The canvas to draw on.
        strength (int): The Wi-Fi signal strength as a percentage.
    """
    center_x = 75
    center_y = 75
    color = "#1E90FF"  # The blue color used in the provided icon

    if strength >= 75:
        draw_arc(canvas, center_x, center_y, 60, color)  # Full strength
        draw_arc(canvas, center_x, center_y, 45, color)
        draw_arc(canvas, center_x, center_y, 30, color)
        draw_circle(canvas, center_x, center_y, 10, color)
    elif strength >= 50:
        draw_arc(canvas, center_x, center_y, 60, "#CCCCCC")
        draw_arc(canvas, center_x, center_y, 45, color)  # Medium strength
        draw_arc(canvas, center_x, center_y, 30, color)
        draw_circle(canvas, center_x, center_y, 10, color)
    elif strength >= 25:
        draw_arc(canvas, center_x, center_y, 60, "#CCCCCC")
        draw_arc(canvas, center_x, center_y, 45, "#CCCCCC")
        draw_arc(canvas, center_x, center_y, 30, color)  # Weak strength
        draw_circle(canvas, center_x, center_y, 10, color)
    else:
        draw_arc(canvas, center_x, center_y, 60, "#CCCCCC")
        draw_arc(canvas, center_x, center_y, 45, "#CCCCCC")
        draw_arc(canvas, center_x, center_y, 30, "#CCCCCC")
        draw_circle(canvas, center_x, center_y, 10, color)  # Poor strength

def draw_no_wifi_icon(canvas):
    """
    Draws the "no Wi-Fi" icon.
    Args:
        canvas (tk.Canvas): The canvas to draw on.
    """
    center_x = 75
    center_y = 75
    color = "#FF0000"  # Red color for the "no Wi-Fi" icon

    # Draw a red cross
    canvas.create_line(center_x - 30, center_y - 30, center_x + 30, center_y + 30, fill=color, width=6)
    canvas.create_line(center_x - 30, center_y + 30, center_x + 30, center_y - 30, fill=color, width=6)

    # Draw a circle to symbolize the Wi-Fi being crossed out
    draw_circle(canvas, center_x, center_y, 40, color)

def draw_arc(canvas, center_x, center_y, radius, color):
    """
    Draws an arc on the canvas.
    Args:
        canvas (tk.Canvas): The canvas to draw on.
        center_x (int): The x-coordinate of the center.
        center_y (int): The y-coordinate of the center.
        radius (int): The radius of the arc.
        color (str): The color of the arc.
    """
    x0 = center_x - radius
    y0 = center_y - radius
    x1 = center_x + radius
    y1 = center_y + radius
    canvas.create_arc(x0, y0, x1, y1, start=0, extent=180, style=tk.ARC, outline=color, width=6)

def draw_circle(canvas, center_x, center_y, radius, color):
    """
    Draws a circle on the canvas.
    Args:
        canvas (tk.Canvas): The canvas to draw on.
        center_x (int): The x-coordinate of the center.
        center_y (int): The y-coordinate of the center.
        radius (int): The radius of the circle.
        color (str): The color of the circle.
    """
    x0 = center_x - radius
    y0 = center_y - radius
    x1 = center_x + radius
    y1 = center_y + radius
    canvas.create_oval(x0, y0, x1, y1, outline=color, width=6)