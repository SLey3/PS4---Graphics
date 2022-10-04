# File: Pyramid.py
# Name: your name

"""
This program draws a pyramid consisting of staggered rows of bricks,
each of which has the dimensions BRICK_WIDTH x BRICK_HEIGHT.  The
base of the pyramid consists of BRICKS_IN_BASE bricks, with each
successive layer one step shorter.  The pyramid is centered in the
graphics window.
"""

from pgl import GWindow, GRect

# Constants (changing these constants should change the picture)

GWINDOW_WIDTH = 500
GWINDOW_HEIGHT = 300
BRICK_WIDTH = 30
BRICK_HEIGHT = 14
BRICKS_IN_BASE = 15

def pyramid():
    """Draws a pyramid on the graphics window."""
    gw = GWindow(GWINDOW_WIDTH, GWINDOW_HEIGHT)
    # You fill in the rest

# Startup code

if __name__ == "__main__":
    pyramid()
