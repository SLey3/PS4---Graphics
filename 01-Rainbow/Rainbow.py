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
    return circle

def rainbow():
    """Displays a rainbow on the graphics window."""
    # Background
    background = GRect(gw.DEFAULT_WIDTH, gw.DEFAULT_HEIGHT)
    background.set_color("SkyBlue")
    background.set_filled(True)
    background.send_to_back()

    gw.add(background)

    for h in range(gw.DEFAULT_HEIGHT + 1):
        for c in rainbow_colors:
            for w in range(gw.DEFAULT_WIDTH + 1):
                c = create_rainbow_line(w, h, 10, 10, c)
                gw.add(c)
# ------------------------------




# Startup code

if __name__ == "__main__":
    rainbow()
