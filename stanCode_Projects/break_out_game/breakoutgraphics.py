"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

This program is to play a Breakout game.
Users can eliminate the bricks by moving
the paddle to bounce the ball and hit the
bricks. The game will end when all the
bricks are eliminated or run out of lives.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40  # Height of a brick (in pixels).
BRICK_HEIGHT = 15  # Height of a brick (in pixels).
BRICK_ROWS = 10  # Number of rows of bricks.
BRICK_COLS = 10  # Number of columns of bricks.
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10  # Radius of the ball (in pixels).
PADDLE_WIDTH = 75  # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels).
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball.

# Global Variable
click = True  # This is to control if the mouseclick is active


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_rows * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_cols * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(PADDLE_WIDTH, PADDLE_HEIGHT, x=(self.window.width - paddle_width) / 2,
                            y=self.window.height - paddle_offset - paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius * 2, ball_radius * 2, x=self.window.width / 2 - ball_radius,
                          y=self.window.height / 2 - ball_radius)
        self.ball.filled = True
        self.window.add(self.ball)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Draw bricks
        self.brick_rows = brick_rows
        self.brick_cols = brick_cols
        self.brick_width = brick_width
        self.brick_height = brick_height
        self.brick_spacing = brick_spacing
        self.brick_offset = brick_offset

        self.draw_bricks()

        # Initialize our mouse listeners
        onmouseclicked(self.start_game)
        onmousemoved(self.change_paddle_position)

    def draw_bricks(self):
        """Draw bricks in the window"""
        for i in range(self.brick_rows):
            for j in range(self.brick_cols):
                brick = GRect(self.brick_width, self.brick_height)
                brick.filled = True
                if j // 2 == 0:   # column = 10, num_color = 5, 10 / 5 = 2
                    # red
                    brick.fill_color = 'red'
                elif j // 2 == 1:
                    # orange
                    brick.fill_color = 'orange'
                elif j // 2 == 2:
                    # yellow
                    brick.fill_color = 'yellow'
                elif j // 2 == 3:
                    # green
                    brick.fill_color = 'green'
                elif j // 2 == 4:
                    # blue
                    brick.fill_color = 'blue'
                # end = j % 10
                # if end == 0 or end == 1:
                #     brick.fill_color = 'red'
                # elif end == 2 or end == 3:
                #     brick.fill_color = 'orange'
                # elif end == 4 or end == 5:
                #     brick.fill_color = 'yellow'
                # elif end == 6 or end == 7:
                #     brick.fill_color = 'green'
                # else:
                #     brick.fill_color = 'blue'
                brick_x = (self.brick_width + self.brick_spacing) * i
                brick_y = self.brick_offset + (self.brick_height + self.brick_spacing) * j
                if self.window.get_object_at(brick_x, brick_y) is None:
                    self.window.add(brick, x=brick_x, y=brick_y)

    def start_game(self, event1):
        """Start the game"""
        global click
        if self.check_ball_position():
            if click:
                if 0 < event1.x < self.window.width and 0 < event1.y < self.window.height:
                    self.set_ball_x_velocity()
                    click = False

    def check_ball_position(self):
        """Check if the ball position is in the window"""
        if 0 < self.ball.x < self.window.width:
            if 0 < self.ball.y < self.window.height:
                return True

    def set_ball_x_velocity(self):
        """
        Set ball x velocity to random negative or positive number
        Set ball y velocity to INITIAL_Y_SPEED
        """
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx
        self.__dy = INITIAL_Y_SPEED

    def change_paddle_position(self, event2):
        """Set the paddle to move with the mouse"""
        # if event2.x - self.paddle.width / 2 <= 0:
        #     self.paddle.x = 0
        # elif event2.x + self.paddle.width / 2 >= self.window.width:
        #     self.paddle.x = self.window.width - self.paddle.width
        # else:
        #     self.paddle.x = event2.x - self.paddle.width / 2
        if self.paddle.width / 2 <= event2.x <= self.window.width - self.paddle.width / 2:
            self.paddle.x = event2.x - self.paddle.width / 2

    def below_bottom(self):
        """Check if the ball position is beneath the bottom of the window"""
        return self.ball.y >= self.window.height

    def reset(self):
        """Reset the ball and the bricks in the window"""
        global click
        if self.check_ball_position() is not True:
            click = True
            self.window.add(self.ball, x=(self.window.width - self.ball.width) / 2,
                            y=(self.window.height - self.ball.height) / 2)
            self.draw_bricks()
            self.__dx = 0
            self.__dy = 0
            onmouseclicked(self.start_game)

    def handle_wall_collisions(self):
        """Update __dx and __dy depending on whether or not the ball has hit a wall"""
        if self.ball.x <= 0 or self.ball.x + self.ball.width > self.window.width:
            self.__dx = -self.__dx
        if self.ball.y <= 0:
            # hit bottom won't bounce
            self.__dy = -self.__dy

    def handle_collisions(self):
        """Update __dy and eliminate a brick depending on the ball has hit the paddle or a brick"""
        x1 = self.ball.x
        y1 = self.ball.y
        x2 = self.ball.x + self.ball.width
        y2 = self.ball.y + self.ball.height
        obj_1 = self.window.get_object_at(x1, y1)
        obj_2 = self.window.get_object_at(x2, y1)
        obj_3 = self.window.get_object_at(x2, y2)
        obj_4 = self.window.get_object_at(x1, y2)
        if obj_1 is not None:
            if obj_1.y < self.paddle.y:
                # hit brick
                self.window.remove(obj_1)
            self.__dy = -self.__dy
            self.ball.move(self.__dx, self.__dy)
        elif obj_2 is not None:
            if obj_2.y < self.paddle.y:
                # hit brick
                self.window.remove(obj_2)
            self.__dy = -self.__dy
            self.ball.move(self.__dx, self.__dy)
        elif obj_3 is not None:
            if obj_3.y < self.paddle.y:
                # hit brick
                self.window.remove(obj_3)
            self.__dy = -self.__dy
            self.ball.move(self.__dx, self.__dy)
        elif obj_4 is not None:
            if obj_4.y < self.paddle.y:
                # hit brick
                self.window.remove(obj_4)
            self.__dy = -self.__dy
            self.ball.move(self.__dx, self.__dy)

    def get_x_velocity(self):
        """Get __dx"""
        return self.__dx

    def get_y_velocity(self):
        """Get __dy"""
        return self.__dy

    def still_have_brick(self):
        """Check if still have bricks in the window"""
        for i in range(self.brick_rows):
            for j in range(self.brick_cols):
                brick_x = (self.brick_width + self.brick_spacing) * i
                brick_y = self.brick_offset + (self.brick_height + self.brick_spacing) * j
                if self.window.get_object_at(brick_x, brick_y) is not None:
                    return True


