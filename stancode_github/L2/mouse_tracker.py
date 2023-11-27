"""
File: mouse_tracker.py
Name:
------------------------
This file shows how to use campy
mouse event to draw GOval
"""

from campy.graphics.gobjects import GRect, GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmousemoved, onmouseclicked, onmousedragged

# This constant controls the size of the GRect
SIZE = 100

rect = GRect(SIZE/2, SIZE/2)
window = GWindow()


def main():
	onmousemoved(tracker)
	onmouseclicked(draw)
	onmousedragged(draw)
	rect.filled = True
	window.add(rect)


def tracker(mouse):
	rect.x = mouse.x-SIZE/2
	rect.y = mouse.y-SIZE/2


def draw(mouse):
	hole = GOval(SIZE/2, SIZE/2)
	hole.filled = True
	window.add(hole, x=mouse.x-SIZE/2, y=mouse.y-SIZE/2)


if __name__ == '__main__':
	main()
