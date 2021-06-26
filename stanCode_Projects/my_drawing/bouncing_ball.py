"""
File: bouncing_ball.py
Name: Claire Yang
-------------------------
This program simulates a bouncing ball at (START_X, START_Y)
that has VX as x velocity and 0 as y velocity. Each bounce reduces
y velocity to REDUCE of itself.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

# Constant
VX = 3
DELAY = 20
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

# Global Variable
window = GWindow(800, 500, title='bouncing_ball')   # This is the window
click_count = 0   # This is to check the count of click


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    # start ball
    start_ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
    start_ball.filled = True
    window.add(start_ball)

    # mouseclick
    onmouseclicked(bounce)


def bounce(mouse):
    """
    :param mouse: mouseclick by user
    :return: a bouncing ball start at (START_X, START_Y) that has VX as x velocity and 0 as y velocity
    """
    global click_count
    if click_count < 3:
        check = window.get_object_at(START_X + SIZE / 2, START_Y)
        if check is not None:
            click_count += 1
            window.remove(check)
            ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
            ball.filled = True
            window.add(ball)
            vy = 0
            while True:
                vy += GRAVITY
                ball.move(VX, vy)
                if ball.y >= window.height:
                    vy = - vy * REDUCE
                if ball.x > window.width:
                    break
                pause(DELAY)
            next_ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
            next_ball.filled = True
            window.add(next_ball)


if __name__ == "__main__":
    main()
