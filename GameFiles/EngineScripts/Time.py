import pygame

deltaTime = float(0.0)

last_tick = pygame.time.get_ticks()


def update():
	global deltaTime, last_tick

	tick = pygame.time.get_ticks()

	deltaTime = (tick - last_tick) / 1000.0

	last_tick = tick
