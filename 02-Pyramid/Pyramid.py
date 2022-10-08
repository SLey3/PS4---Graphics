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

    gw.bricks_in_base = BRICKS_IN_BASE

    line = ""
    
    compound = GCompound()
    
    gw.X = GWINDOW_WIDTH - 450 # base x_cord
    gw.x_cord = gw.X # x_cord that will be later modified
    gw.x_increment = 15
    gw.y_cord = 260
    for _ in range(gw.bricks_in_base+1):
        for b in range(gw.bricks_in_base+1):
            compound.add(create_pyramid_block(gw.x_cord, gw.y_cord))
            gw.x_cord += 30
        gw.bricks_in_base = gw.bricks_in_base - 1
        gw.x_cord = gw.X + gw.x_increment
        gw.x_increment = gw.x_increment + 15
        gw.y_cord -= 15
    
    gw.add(compound)


# Startup code

if __name__ == "__main__":
    pyramid()
