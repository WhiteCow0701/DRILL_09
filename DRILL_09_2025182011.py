from pico2d import *


SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 1024
background = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
running = True
x, y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
frame = 0


open_canvas(SCREEN_WIDTH, SCREEN_HEIGHT)


while running:
	clear_canvas()
	background.draw(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
	character.clip_draw(frame * 100, 100, 100, 100, x, y)
	update_canvas()
	delay(0.05)


close_canvas()
