import pygame

from GameFiles.EngineScripts.GameObject import GameObject


class Frogger(GameObject):

	def __init__(self, game_display):
		super().__init__(game_display)
		self.vector2 = [500, 500]
		self.color = (0, 255, 0)

	def update(self, event_list):
		for event in event_list:
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP or event.key == pygame.K_w:
					self.vector2 = [self.vector2[0], self.vector2[1] - 20]

		super().render()
