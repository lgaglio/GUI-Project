from abc import ABC, abstractclassmethod


class GameObject(ABC):

	def __init__(self, game_display):
		self.vector2 = [0, 0]
		self.display = game_display
		self.size = 20
		self.color = (0, 0, 0)

	@abstractclassmethod
	def update(self):
		pass

	def render(self):
		self.display.fill(self.color, rect=[self.vector2[0], self.vector2[1], self.size, self.size])
