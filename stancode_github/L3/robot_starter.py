from campy.graphics.gobjects import GOval
from robot import Robot, Robot2, Robot3
from campy.graphics.gwindow import GWindow

print('robot_starter.py(__name___:)', __name__)


def main():
    window = GWindow()
    r1 = Robot(185, 70)
    ball = r1.give_me_a_ball(50)
    window.add(ball)
    r1.self_intro()
    r1.bmi()
    Robot.say_hi()
    r1.say_hi()
    r2 = Robot2(150, 90)
    ball2 = r2.give_me_a_ball(30)
    window.add(ball2)
    r2.start_count()
    r3 = Robot3(178, 80, 'yellow', count3=5)
    r3.start_count()
    rect3 = r3.give_me_a_rect(70)
    window.add(rect3)


if __name__ == '__main__':
    main()
