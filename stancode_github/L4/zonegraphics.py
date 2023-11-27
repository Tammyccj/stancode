from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect
from campy.gui.events.mouse import onmouseclicked
import random

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
ZONE_WIDTH = 100
ZONE_HEIGHT = 100
BALL_RADIUS = 15
MAX_SPEED = 6
MIN_Y_SPEED = 2


class ZoneGraphics:

    def __init__(self, window_width=WINDOW_WIDTH, window_height=WINDOW_HEIGHT,
                 zone_width=ZONE_WIDTH, zone_height=ZONE_HEIGHT, ball_radius=BALL_RADIUS):
        # Create window
        self.window = GWindow(width=window_width, height=window_height, title='Zone game')

        # Create zone
        self.zone = GRect(zone_width, zone_height)
        self.window.add(self.zone, x=(self.window.width-self.zone.width)/2, y=(self.window.height-self.zone.height)/2)

        # Create ball and initialize velocity/position
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.set_ball_position()
        self.window.add(self.ball)
        onmouseclicked(self.set_new_position)

    def set_ball_position(self):
        random_x = random.randint(0, self.window.width-self.ball.width)
        random_y = random.randint(0, self.window.height-self.ball.height)
        while self.zone.x <= random_x <= self.zone.x + self.zone.width or self.zone.y <= random_y <= self.zone.y + self.zone.height:
            random_x = random.randint(0, self.window.width-self.ball.width)
            random_y = random.randint(0, self.window.height - self.ball.height)
        self.ball.x = random_x
        self.ball.y = random_y

    @staticmethod
    def get_vx():
        return random.randint(0, MAX_SPEED)

    @staticmethod
    def get_vy():
        return random.randint(MIN_Y_SPEED, MAX_SPEED)

        # Initialize mouse listeners
    def set_new_position(self, mouse):
        obj = self.window.get_object_at(mouse.x, mouse.y)
        if obj == self.ball:
            random_x2 = random.randint(0, self.window.width - self.ball.width)
            random_y2 = random.randint(0, self.window.height - self.ball.height)
            while self.zone.x <= random_x2 <= self.zone.x + self.zone.width or self.zone.y <= random_y2 <= self.zone.y + self.zone.height:
                random_x2 = random.randint(0, self.window.width - self.ball.width)
                random_y2 = random.randint(0, self.window.height - self.ball.height)
            self.ball.x = random_x2
            self.ball.y = random_y2










