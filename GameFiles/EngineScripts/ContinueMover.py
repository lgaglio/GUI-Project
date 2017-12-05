from GameFiles.EngineScripts import Time
from GameFiles.EngineScripts.GameObject import GameObject


class ContinueMover(GameObject):
	"""
	Direction must be a number.
	0 = up
	1 = down
	2 = left
	3 = right
	"""

	def __init__(self, game_display, direction, speed):
		super().__init__(game_display)
		self.speed = speed
		self.direction = direction

	def update(self):
		if self.direction == 0:
			self.vector2[1] -= self.speed * Time.deltaTime
		elif self.direction == 1:
			self.vector2[1] += self.speed * Time.deltaTime
		elif self.direction == 2:
			self.vector2[0] -= self.speed * Time.deltaTime
		elif self.direction == 3:
			self.vector2[0] += self.speed * Time.deltaTime

		super().render()
