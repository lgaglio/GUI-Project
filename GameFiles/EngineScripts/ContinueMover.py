from GameFiles.EngineScripts import Time
from GameFiles.EngineScripts.GameObject import GameObject
from GameFiles.EngineScripts.HitBox import HitBox


class ContinueMover(GameObject):
	"""
	This class moves an object for as long as the update method is called.
	function:: __init__(self, game_display, direction, speed, color=(0,0,0))

	Direction must be a number.
	0 = up
	1 = down
	2 = left
	3 = right
	"""
	def __init__(self, game_display, direction, speed, color=(0, 0, 0)):
		# Calls the super's init function to set it's things up.
		super().__init__(game_display, color)
		# Set's the speed to the passed speed
		self.speed = speed
		# Set's the direction of movement.
		self.direction = direction
		# Set's the y value of the Vector2.
		self.lead_vertex.y = 5
		# Set's the x and y value of the Vector2
		self.size.x = 50
		self.size.y = 22
		# Set up's the hitbox.
		self.hitbox = HitBox(self, self.lead_vertex, self.size)

	def update(self):
		if self.direction == 0:
			self.lead_vertex.y -= self.speed * Time.deltaTime

			if self.lead_vertex.y + self.size.y <= 0:
				self.lead_vertex.y = 600
		elif self.direction == 1:
			self.lead_vertex.y += self.speed * Time.deltaTime

			if self.lead_vertex.y >= 800:
				self.lead_vertex.y = 0 - self.size.y
		elif self.direction == 2:
			self.lead_vertex.x -= self.speed * Time.deltaTime

			if self.lead_vertex.x + self.size.x <= 0:
				self.lead_vertex.x = 800
		elif self.direction == 3:
			self.lead_vertex.x += self.speed * Time.deltaTime

			if self.lead_vertex.x >= 800:
				self.lead_vertex.x = 0 - self.size.x

	def on_enter(self, other_game_object):
		return

	def on_exit(self, other_game_object):
		return
