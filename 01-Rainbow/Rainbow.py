# File: Rainbow.py
# Name: Sergio Ley Languren

"""
This program defines the function rainbow, which displays a rainbow on
the graphics window.
"""

from pgl import GWindow, GOval, GRect

gw = GWindow()


rainbow_colors = [
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "indigo",
    "violet"
]

def create_rainbow_line(x, y, h, w, color):
    circle = GOval(x, y, w, h)
    circle.set_color(color)
    circle.set_filled(True)
    
    rect = GRect(x, y, w, h)
    rect.set_color(color)
    rect.set_filled(True)
    return circle, rect

def rainbow():
    """Displays a rainbow on the graphics window."""
    h = 1
    for c in rainbow_colors:
        for w in range(gw.DEFAULT_WIDTH + 1):
            cr, rc = create_rainbow_line(w, h, 50, 50, c)
            gw.add(cr)
            gw.add(rc)
        h += 50
# ------------------------------




# Startup code

if __name__ == "__main__":
    rainbow()
