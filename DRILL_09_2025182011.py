from pico2d import *


SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 1024
MOVE_SPEED = 5
FRAME_DELAY = 0.05
open_canvas(SCREEN_WIDTH, SCREEN_HEIGHT)
background = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
running = True
x, y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
frame = 0
keys = {SDLK_LEFT: False, SDLK_RIGHT: False, SDLK_UP: False, SDLK_DOWN: False}
character_row = 0
moving = False


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


def update_position():
	global x, y, character_row, moving

	moving = any(keys.values())

	if keys[SDLK_LEFT]:
		x -= MOVE_SPEED
		character_row = 3
	if keys[SDLK_RIGHT]:
		x += MOVE_SPEED
		character_row = 2
	if keys[SDLK_UP]:
		y += MOVE_SPEED
	if keys[SDLK_DOWN]:
		y -= MOVE_SPEED

	x = clamp(50, x, SCREEN_WIDTH - 50)
	y = clamp(50, y, SCREEN_HEIGHT - 50)


def animation_row():
	if moving:
		return character_row
	return character_row - 2 if character_row >= 2 else character_row


while running:
	handle_events()
	update_position()
	clear_canvas()
	background.draw(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
	character.clip_draw(frame * 100, animation_row() * 100, 100, 100, x, y)
	update_canvas()
	frame = (frame + 1) % 8
	delay(FRAME_DELAY)


close_canvas()
