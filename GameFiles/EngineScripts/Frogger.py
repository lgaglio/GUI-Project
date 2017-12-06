import pygame

import GameFiles.EngineScripts.Time as Time
from GameFiles.EngineScripts.GameObject import GameObject


class Frogger(GameObject):

	def __init__(self, game_display, main_class):
		super().__init__(game_display)
		self.vector2 = [500, 500]
		self.color = (0, 255, 0)
		self.main_class_link = main_class
		self.button_down = False
		self.speed = 100

	def update(self):
		for event in self.main_class_link.event_list:
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP or event.key == pygame.K_w:
					self.button_down = True
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_UP or event.key == pygame.K_w:
					self.button_down = False

		if self.button_down:
			self.vector2[1] -= self.speed * Time.deltaTime

		super().render()
