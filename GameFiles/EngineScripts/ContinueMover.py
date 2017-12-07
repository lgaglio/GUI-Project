from GameFiles.EngineScripts import Time
from GameFiles.EngineScripts.GameObject import GameObject
from GameFiles.EngineScripts.HitBox import HitBox


class ContinueMover(GameObject):
	"""
	Direction must be a number.
	0 = up
	1 = down
	2 = left
	3 = right
	"""

	def __init__(self, game_display, direction, speed, color=(0, 0, 0)):
		super().__init__(game_display, color)
		self.speed = speed
		self.direction = direction

		self.lead_vertex.y = 5
		self.size.x = 20
		self.size.y = 20

		self.hitbox = HitBox(self, self.lead_vertex, self.size)

	def update(self):
		if self.direction == 0:
			self.lead_vertex.y -= self.speed * Time.deltaTime
		elif self.direction == 1:
			self.lead_vertex.y += self.speed * Time.deltaTime
		elif self.direction == 2:
			self.lead_vertex.x -= self.speed * Time.deltaTime
		elif self.direction == 3:
			self.lead_vertex.x += self.speed * Time.deltaTime

		super().render()
