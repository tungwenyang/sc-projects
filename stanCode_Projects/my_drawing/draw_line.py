"""
File: draw_line.py
Name: Claire Yang
-------------------------
This program creates lines on an instance of GWindow class.
There is a circle indicating the user’s first click. A line appears
at the condition where the circle disappears as the user clicks
on the canvas for the second time.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# This constant controls the size of the GOval
SIZE = 10

# Global Variable
window = GWindow(width=800, height=500, title='draw_line')   # This is the window
count = 0   # This is to check to draw oval or line
circle_x = 0
circle_y = 0


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw)


def draw(mouse):
    """
    :param mouse: mouseclick by user
    :return: draw a circle or a line
    """
    global count
    global circle_x
    global circle_y

    if count % 2 == 0:
        circle = GOval(SIZE, SIZE)
        window.add(circle, mouse.x - SIZE / 2, mouse.y - SIZE / 2)
        count += 1
        circle_x = mouse.x
        circle_y = mouse.y
    else:
        line = GLine(circle_x, circle_y, mouse.x, mouse.y)
        # check if (circle_x + SIZE / 2, circle_y) is circle
        maybe_circle = window.get_object_at(circle_x + SIZE / 2, circle_y)
        if maybe_circle is not None:
            window.remove(maybe_circle)
        window.add(line)
        count += 1


if __name__ == "__main__":
    main()
