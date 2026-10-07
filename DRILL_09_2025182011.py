from pico2d import *


SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 1024
background = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
running = True
x, y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
frame = 0
keys = {SDLK_LEFT: False, SDLK_RIGHT: False, SDLK_UP: False, SDLK_DOWN: False}


def handle_events():
	global running

	for event in get_events():
		if event.type == SDL_QUIT:
			running = False
		elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
			running = False
		elif event.type == SDL_KEYDOWN and event.key in keys:
			keys[event.key] = True
		elif event.type == SDL_KEYUP and event.key in keys:
			keys[event.key] = False


open_canvas(SCREEN_WIDTH, SCREEN_HEIGHT)


while running:
	clear_canvas()
	background.draw(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
	character.clip_draw(frame * 100, 100, 100, 100, x, y)
	update_canvas()
	handle_events()
	frame = (frame + 1) % 8
	delay(0.05)
	delay(0.05)


close_canvas()
