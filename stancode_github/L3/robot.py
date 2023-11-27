
from campy.graphics.gobjects import GOval, GRect

print('robot.py(__name__): ', __name__)

class Robot:
    # constructor
    def __init__(self, height, weight, color='blue'):
        self.h = height
        self.w = weight
        self.c = color

    # method
    def give_me_a_ball(self,size):
        ball = GOval(size, size)
        ball.filled = True
        ball.fill_color = self.c
        return ball

    def self_intro(self):
        print(f'h={self.h}/ w={self.w}')

    def bmi(self):
        height_in_meter = self.h/100
        print('BMI:', self.w/(height_in_meter**2))

    @staticmethod
    def say_hi():
        print('Hi')


class Robot2(Robot):
    def __init__(self, height2, weight2, color2='green', count2=3):
        super().__init__(height2, weight2, color=color2)
        self.count = count2

    def start_count(self):
        for i in range(self.count):
            print(i+1)


class Robot3(Robot2):
    def __init__(self, height3, weight3, rect_color, color3='green', count3=3):
        super().__init__(height3, weight3, color2=color3, count2=count3)
        self.r_c = rect_color

    def give_me_a_rect(self, size):
        rect = GRect(size, size)
        rect.filled = True
        rect.fill_color = self.r_c
        return rect
