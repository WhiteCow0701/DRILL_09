from pico2d import *


SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 1024
running = True


open_canvas(SCREEN_WIDTH, SCREEN_HEIGHT)


while running:
	clear_canvas()
	update_canvas()
	delay(0.05)


close_canvas()
