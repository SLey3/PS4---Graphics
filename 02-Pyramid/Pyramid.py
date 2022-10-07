# File: Pyramid.py
# Name: Sergio Ley Languren

"""
This program draws a pyramid consisting of staggered rows of bricks,
each of which has the dimensions BRICK_WIDTH x BRICK_HEIGHT.  The
base of the pyramid consists of BRICKS_IN_BASE bricks, with each
successive layer one step shorter.  The pyramid is centered in the
graphics window.
"""

from pgl import GWindow, GRect, GCompound

# Constants (changing these constants should change the picture)

GWINDOW_WIDTH = 500
GWINDOW_HEIGHT = 300
BRICK_WIDTH = 30
BRICK_HEIGHT = 14
BRICKS_IN_BASE = 12

def create_pyramid_block(x,y):
    """Creates a block of the pyramid. The basic material"""
    rect = GRect(x, y, BRICK_WIDTH, BRICK_HEIGHT)
    rect.set_color("black")
    return rect

def pyramid():
    """Draws a pyramid on the graphics window."""
    gw = GWindow(GWINDOW_WIDTH, GWINDOW_HEIGHT)
    # You fill in the rest
    line = ""
    
    # compound = GCompound()
    
    # count = 0
    
    # for y_cord in range(GWINDOW_HEIGHT + 1):
    #     x_cord = (GWINDOW_WIDTH / 2)
    #     compound.add(create_pyramid_block(x_cord, y_cord))
    #     count += 1
    # gw.add(compound)
    
    rect = create_pyramid_block(GWINDOW_WIDTH/2, 0)
    gw.add(rect)


# Startup code

if __name__ == "__main__":
    pyramid()
