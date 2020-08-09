"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

This program makes a game called
"break out".
This program set bricks, the ball, the velocity of ball,
the paddle, and all the items and conditions
which will be used in the "break out" game.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

# Constants: these constants can be changed by users if they want.
BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

# Constants: these constants cannot be changed by users.
INITIAL_Y_SPEED = 7.0  # Initial vertical speed for the ball.
MAX_X_SPEED = 5      # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):
        self.paddle_height = paddle_height
        self.paddle_offset = paddle_offset
        self.ball_radius = ball_radius
        self.brick_amount = brick_rows * brick_cols
        self.__constant_dy = -INITIAL_Y_SPEED

        # Default initial velocity for the ball.
        self.__dx = 0
        self.__dy = 0

        # Create a graphical window, with some extra space.
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # Create a paddle.
        self.paddle = GRect(paddle_width, paddle_height, x=(self.window_width-paddle_width)/2,
                            y=self.window_height-(paddle_height+paddle_offset))
        self.paddle.filled = True
        self.paddle.color = 'deepskyblue'
        self.paddle.fill_color = 'deepskyblue'
        self.window.add(self.paddle)

        # Initialize our mouse listeners.
        onmouseclicked(self.ball_start)
        onmousemoved(self.paddle_move)

        # Center a filled ball in the graphical window.
        self.ball_x = (self.window_width-2*ball_radius)/2
        self.ball_y = (self.window_height-2*ball_radius)/2
        self.ball = GOval(2*ball_radius, 2*ball_radius)
        self.ball.filled = True
        self.window.add(self.ball, x=self.ball_x, y=self.ball_y)

        # Draw bricks.
        brick_x = 0
        brick_y = brick_offset
        color = 'darkorange'
        while brick_y < brick_offset + brick_rows*(brick_height+brick_spacing):
            # Fill one row.
            if brick_x <= self.window_width - brick_width:
                brick = GRect(brick_width, brick_height)
                brick.filled = True
                brick.color = color
                brick.fill_color = color
                self.window.add(brick, x=brick_x, y=brick_y)
                brick_x += (brick_width + brick_spacing)
            # Change to next row.
            else:
                brick_x = 0
                brick_y += (brick_height + brick_spacing)
            # Fill row 3-4's color.
            if brick_offset + 2*(brick_height+brick_spacing) <= brick_y \
                    < brick_offset + 4*(brick_height+brick_spacing):
                color = 'salmon'
            # Fill row 5-6's color.
            elif brick_offset + 4*(brick_height+brick_spacing) <= brick_y \
                    < brick_offset + 6*(brick_height+brick_spacing):
                color = 'lightsalmon'
            # Fill row 7-8's color.
            elif brick_offset + 6*(brick_height+brick_spacing) <= brick_y \
                    < brick_offset + 8*(brick_height+brick_spacing):
                color = 'pink'
            # Fill row 9-10's color.
            elif brick_offset + 8*(brick_height+brick_spacing) <= brick_y \
                    < brick_offset + 10*(brick_height+brick_spacing):
                color = 'lightcoral'
                # Fill row 10+'s color.
            elif brick_offset + 10*(brick_height+brick_spacing) <= brick_y:
                color = 'violet'

    def paddle_move(self, event):
        """
        This function will make the paddle move with the mouse.
        :param event: MouseEvent
        """
        paddle_x = event.x - self.paddle.width/2
        # These condition will limit the paddle. (only move in the window)
        if paddle_x < 0:
            paddle_x = 0
        elif paddle_x > self.window_width - self.paddle.width:
            paddle_x = self.window_width - self.paddle.width
        paddle_y = self.window_height-(self.paddle_height+self.paddle_offset)
        self.window.add(self.paddle, x=paddle_x, y=paddle_y)

    def ball_start(self, event):
        """
        This function will make the ball start moving
        :param event: MouseEvent
        """
        if self.ball.x == self.ball_x and self.ball.y == self.ball_y:
            self.ball_velocity()

    def ball_velocity(self):
        """
        This function will give a random velocity to the ball.
        """
        # Default initial velocity for the ball.
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx
        self.__dy = INITIAL_Y_SPEED

    def reset_ball(self):
        """
        This function will put the ball back to the original place and make it stop.
        """
        self.window.add(self.ball, x=self.ball_x, y=self.ball_y)
        self.__dx = 0
        self.__dy = 0

    def check_touch_obj(self):
        """
        This function will check whether the ball touch any object.
        Also, if the ball touch a brick, this function will remove that brick and make the amount of bricks -1.
        """
        # Check the first point of the ball.
        point_a = self.window.get_object_at(self.ball.x + self.ball_radius, self.ball.y - 1)
        if point_a is not None:
            self.window.remove(point_a)
            self.brick_amount -= 1
            self.__dy = -self.__dy
        else:
            point_b = self.window.get_object_at(self.ball.x - 1, self.ball.y + self.ball_radius)
            # Check the second point of the ball.
            if point_b is not None:
                self.window.remove(point_b)
                self.brick_amount -= 1
                self.__dy = -self.__dy
            else:
                point_c = self.window.get_object_at(self.ball.x + self.ball_radius,
                                                    self.ball.y + self.ball_radius * 2 + 1)
                # Check the third point of the ball.
                if point_c is not None and point_c.y != self.paddle.y:
                    self.window.remove(point_c)
                    self.brick_amount -= 1
                    self.__dy = -self.__dy
                else:
                    point_d = self.window.get_object_at(self.ball.x + self.ball_radius * 2 + 1,
                                                        self.ball.y + self.ball_radius)
                    # Check the last point of the ball.
                    if point_d is not None:
                        self.window.remove(point_d)
                        self.brick_amount -= 1
                        self.__dy = -self.__dy

    def check_touch_paddle(self):
        """
        This function will check whether the ball touch the paddle.
        :return: boolean
        """
        point_c = self.window.get_object_at(self.ball.x + self.ball_radius, self.ball.y + self.ball_radius * 2 + 1)
        if point_c is not None and point_c.y == self.paddle.y:
            return True

    # Getter
    def get_dx(self):
        """
        This function will return a variable. (a velocity)
        :return: self.__dx
        """
        return self.__dx

    # Getter
    def get_dy(self):
        """
        This function will return a variable. (a velocity)
        :return: self.__dy
        """
        return self.__dy

    # Getter
    def get_constant_dy(self):
        """
        This function will return a variable. (a velocity)
        :return: self.__constant_dy
        """
        return self.__constant_dy

    # Setter
    def set_dx(self, new_dx):
        """
        This function will reset the value of self.__dx. (a velocity)
        :param new_dx: a new value which gave by the user.
        """
        self.__dx = new_dx

    # Setter
    def set_dy(self, new_dy):
        """
        This function will reset the value of self.__dy. (a velocity)
        :param new_dy: a new value which gave by the user.
        """
        self.__dy = new_dy
