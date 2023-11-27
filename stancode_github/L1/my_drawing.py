"""
File: my_drawing.py
Name: 
----------------------
This file uses the campy module to
draw on a GWindow object.
"""

from campy.graphics.gobjects import GOval, GRect, GLabel, GPolygon, GArc, GLabel
from campy.graphics.gwindow import GWindow


def main():
    window = GWindow()
    pumpkin_2 = GOval(150, 260)
    pumpkin_2.filled = True
    pumpkin_2.fill_color = 'orangered'
    pumpkin_3 = GOval(150, 260)
    pumpkin_3.filled = True
    pumpkin_3.fill_color = 'orangered'
    pumpkin_1 = GOval(180, 280)
    pumpkin_1.filled = True
    pumpkin_1.fill_color = 'orangered'

    leaf = GPolygon()
    leaf.add_vertex((window.width / 2, (window.height-280)/2+10))
    leaf.add_vertex((window.width / 2-12, (window.height - 280) / 2-25))
    leaf.add_vertex((window.width / 2+12, (window.height - 280) / 2-25))
    leaf.filled = True
    leaf.fill_color = 'forestgreen'

    l_eye = GPolygon()
    l_eye.add_vertex((window.width/2-35, (window.height-50)/2))
    l_eye.add_vertex((window.width/2-85, (window.height-50)/2))
    l_eye.add_vertex((window.width/2-60, (window.height-50)/2-40))
    l_eye.filled = True

    r_eye = GPolygon()
    r_eye.add_vertex((window.width / 2 + 35, (window.height - 50) / 2))
    r_eye.add_vertex((window.width / 2 + 85, (window.height - 50) / 2))
    r_eye.add_vertex((window.width / 2 + 60, (window.height - 50) / 2 - 40))
    r_eye.filled = True

    nose = GPolygon()
    nose.add_vertex((window.width /2-10, window.height/2+10))
    nose.add_vertex((window.width /2+10, window.height/2+10))
    nose.add_vertex((window.width /2, window.height/2-10))
    nose.filled = True

    mouth = GArc(150, 70, 180, 180)
    mouth.filled = True

    text = GLabel('HALLOWEEN')
    text.font = '-55'
    window.add(text, x=40, y=window.height)

    window.add(leaf)
    window.add(pumpkin_2, (window.width-180)/2-90, (window.height-280)/2+15)
    window.add(pumpkin_3, (window.width-180)/2+130, (window.height-280)/2+15)
    window.add(pumpkin_1, (window.width-180)/2, (window.height - 280)/2)
    window.add(l_eye)
    window.add(r_eye)
    window.add(nose)
    window.add(mouth, x=window.width/2-75, y=window.height/2+40)

if __name__ == '__main__':
    main()
