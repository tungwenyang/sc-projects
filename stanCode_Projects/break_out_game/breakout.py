"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

This program is to play a Breakout game.
Users can eliminate the bricks by moving
the paddle to bounce the ball and hit the
bricks. The game will end when all the
bricks are eliminated or run out of lives.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3			 # Number of attempts


def main():
    """
    This program is to play a Breakout game. Users can eliminate the bricks by moving the paddle to bounce the ball
    and hit the bricks. The game will end when all the bricks are eliminated or run out of lives.
    """
    graphics = BreakoutGraphics()
    lives = NUM_LIVES

    # Add animation loop
    while True:
        # Pause
        pause(FRAME_RATE)

        # Check
        # Stop looping if all the bricks are eliminated
        if not graphics.still_have_brick():
            break
        # Lose one life if the ball falls out of the bottom of the window
        if graphics.below_bottom():
            lives -= 1
            if lives > 0:
                graphics.reset()
            # Stop looping if no lives left
            else:
                break
        # The ball will bounce if it hits the wall
        graphics.handle_wall_collisions()
        # The ball will eliminate the brick and bounce if it hits the brick, and will bounce if it hits the paddle
        graphics.handle_collisions()

        # Move
        ball_vx = graphics.get_x_velocity()
        ball_vy = graphics.get_y_velocity()
        graphics.ball.move(ball_vx, ball_vy)


if __name__ == '__main__':
    main()
