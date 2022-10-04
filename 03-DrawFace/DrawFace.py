# File: DrawFace.py
# Name: your name

"""
This program draws a face on the window in which the eyes follow the
mouse.
"""

import math
from pgl import GWindow, GLine, GOval, GRect, GPolygon

# Constants

GWINDOW_WIDTH = 500                   # Width of the graphics window
GWINDOW_HEIGHT = 400                  # Height of the graphics window
FACE_WIDTH = 200                      # Width of the face in pixels
FACE_HEIGHT = 300                     # Height of the face in pixels
EYE_WIDTH = 0.15 * FACE_WIDTH         # Width of eye relative to face
EYE_HEIGHT = 0.15 * FACE_HEIGHT       # Height of eye relative to face
NOSE_WIDTH = 0.15 * FACE_WIDTH        # Width of nose relative to face
NOSE_HEIGHT = 0.10 * FACE_HEIGHT      # Height of nose relative to face
MOUTH_WIDTH = 0.50 * FACE_WIDTH       # Width of mouth relative to face
MOUTH_HEIGHT = 0.03 * FACE_HEIGHT     # Height of mouth relative to face
PUPIL_RADIUS = 0.2 * EYE_WIDTH        # Pupil radius relative to eye

# Main program

def draw_face():
    """Draws a face in which the eyes track the mouse."""
    # You fill in the code

# Startup code

if __name__ == "__main__":
    draw_face()
