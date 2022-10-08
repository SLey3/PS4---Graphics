# File: DrawFace.py
# Name: Sergio Ley Languren

"""
This program draws a face on the window in which the eyes follow the
mouse.
"""

from pgl import GWindow, GLine, GOval, GRect, GPolygon, GCompound
from math import sqrt

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
EYE_SEP = FACE_WIDTH * 0.4
PUPIL_HEIGHT_CENTER_SEP = EYE_HEIGHT * 0.5
PUPIL_WIDTH_CENTER_SEP = EYE_WIDTH * 0.1


# Main program


# sqrt((x**2) + (y**2))

def create_triangle() -> GPolygon:
    """Creates a triangle polygon"""
    tri = GPolygon()

    tri.add_vertex(-NOSE_WIDTH/2, NOSE_HEIGHT/2)
    tri.add_vertex(NOSE_WIDTH/2, NOSE_HEIGHT/2)
    tri.add_vertex(0, -NOSE_HEIGHT/2)
    tri.set_visible(True)
    tri.set_color("black")
    tri.set_line_width(2)
    return tri


def create_eyes(gw):
    """Creates the eyes"""
    eye1 = GOval((GWINDOW_WIDTH/2) - EYE_SEP/2 - EYE_WIDTH/2, (GWINDOW_HEIGHT/2) - 100, EYE_WIDTH, EYE_HEIGHT)
    eye1.set_color("black")
    eye1.set_line_width(1)
    eye1.set_visible(True)
    pupil1 = GOval((GWINDOW_WIDTH/2) - EYE_SEP/2 - PUPIL_WIDTH_CENTER_SEP, (GWINDOW_HEIGHT/2) - EYE_SEP/2 - PUPIL_HEIGHT_CENTER_SEP*2, PUPIL_RADIUS, PUPIL_RADIUS)
    pupil1.set_color("black")
    pupil1.set_filled(True)

    eye2 = GOval((GWINDOW_WIDTH/2) + EYE_SEP/2 - EYE_WIDTH/2, (GWINDOW_HEIGHT/2) - 100, EYE_WIDTH, EYE_HEIGHT)
    eye2.set_color("black")
    eye2.set_line_width(1)
    eye1.set_visible(True)
    pupil2 = GOval((GWINDOW_WIDTH/2) + EYE_SEP/2 - PUPIL_WIDTH_CENTER_SEP, (GWINDOW_HEIGHT/2) - EYE_SEP/2 - PUPIL_HEIGHT_CENTER_SEP*2, PUPIL_RADIUS, PUPIL_RADIUS)
    pupil2.set_color("black")
    pupil2.set_filled(True)
    
    gw.pupil1 = pupil1
    gw.pupil2 = pupil2
    
    gw.lx0 = (GWINDOW_WIDTH/2) - EYE_SEP/2 - PUPIL_WIDTH_CENTER_SEP
    gw.rx0 = (GWINDOW_WIDTH/2) + EYE_SEP/2 - PUPIL_WIDTH_CENTER_SEP
    gw.y0 = (GWINDOW_HEIGHT/2) - EYE_SEP/2 - PUPIL_HEIGHT_CENTER_SEP*2
    
    return eye1, pupil1, eye2, pupil2
    


def draw_face():
    """Draws a face in which the eyes track the mouse."""

    gw = GWindow(GWINDOW_WIDTH, GWINDOW_HEIGHT)

    face_compound = GCompound()
    
    gw.face_compound = face_compound

    face = GOval(GWINDOW_WIDTH/2 - FACE_WIDTH/2, GWINDOW_HEIGHT/2 - FACE_HEIGHT/2, FACE_WIDTH, FACE_HEIGHT)
    face.set_color("black")
    face.set_line_width(1)
    face_compound.add(face)

    tri = create_triangle()
    face_compound.add(tri, GWINDOW_WIDTH/2, GWINDOW_HEIGHT/2)

    mouth = GRect((GWINDOW_WIDTH/2) - 50, (FACE_HEIGHT*2)/2, MOUTH_WIDTH, MOUTH_HEIGHT)
    mouth.set_color("black")
    mouth.set_line_width(1)
    face_compound.add(mouth)
    
    eye1, pupil1, eye2, pupil2 = create_eyes(gw)

    face_compound.add(eye1)
    face_compound.add(pupil1)
    face_compound.add(eye2)
    face_compound.add(pupil2)
    
    def pupilsanimation(e):
        """animates the first pupil"""
        x_cord = e.get_x()
        y_cord = e.get_y()
        
        restriction = sqrt((gw.lx0**2) + (gw.y0**2))
        print(f"restriction: {restriction}")
        gw.pupil1.set_bounds(
            min(x_cord, gw.lx0, restriction),
            min(y_cord, gw.y0, restriction),
            abs(x_cord - gw.lx0),
            abs(y_cord - gw.y0)
        )
    
    gw.add_event_listener("mousemove", pupilsanimation)


    gw.add(face_compound)

# Startup code

if __name__ == "__main__":
    draw_face()
