"""
File: center_me.py
Name: Jerry Liao
--------------------------------
This program shows how to center a GRect
on the window where the width and the height are
randomly chosen
"""

from campy.graphics.gobjects import GRect
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause

SIZE = 100       # Controls the width and height of the rect
WIDTH = 800      # Controls the width of the window
HEIGHT = 500     # Controls the height of the window


def main():
    """
    Center a magenta rect on the canvas
    where the width and height are SIZE
    """
    window = GWindow(width=WIDTH, height=HEIGHT, title='CenterMe')
    rect = GRect(SIZE, SIZE, x=(window.width-SIZE)/2, y=(window.height-SIZE)/2)
    rect.filled = True
    rect.fill_color = 'magenta'
    rect.color = 'magenta'
    rect_2 = GRect(SIZE, SIZE, x=(window.width-SIZE)/2, y=(window.height-SIZE)/2)
    rect_2.filled = True
    rect_2.fill_color = 'yellow'
    window.add(rect)
    window.add(rect_2)
    vx = 5
    vy = 5
    switch = True
    while True:
        rect.move(vx, 0)
        rect_2.move(0, vy)
        if rect.x <= 0 or rect.x+rect.width >= window.width:
            vx = -vx
            if switch:
                rect.fill_color = 'blue'
                switch = False
            else:
                rect.fill_color = 'magenta'
                switch = True
        if rect_2.y <= 0 or rect_2.y+rect_2.height >= window.height:
            vy = -vy
        pause(10)


if __name__ == '__main__':
    main()
