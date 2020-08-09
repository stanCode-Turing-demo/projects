"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

This program plays a game called
"break out" in which players
moving the paddle to make the ball bounce
and break all bricks!
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

# Constants
FRAME_RATE = 2000 / 120  # 120 frames per second.
NUM_LIVES = 3  # The number of lives.


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    constant_dy = graphics.get_constant_dy()
    # This condition can control when the game will stop. (die or win)
    while lives > 0 and graphics.brick_amount > 0:
        dx = graphics.get_dx()
        dy = graphics.get_dy()
        graphics.ball.move(dx, dy)
        pause(FRAME_RATE)
        # If the ball touch the left or right wall, it will bounce.
        if graphics.ball.x < 0 or graphics.ball.x + graphics.ball.width > graphics.window_width:
            graphics.set_dx(-dx)
        # If the ball touch the top wall, it will bounce.
        elif graphics.ball.y < 0:
            graphics.set_dy(-dy)
        # If the ball touch the ground, lives-1 and the ball will be reset.
        elif graphics.ball.y + graphics.ball.height > graphics.window_height:
            lives -= 1
            graphics.reset_ball()
        # If the ball touch the brick, the brick will be removed and the ball will bounce.
        elif graphics.ball.y + graphics.ball.height < graphics.paddle.y:
            graphics.check_touch_obj()
        # If the ball touch the paddle, the ball will bounce.
        elif graphics.check_touch_paddle():
            graphics.set_dy(constant_dy)


if __name__ == '__main__':
    main()
