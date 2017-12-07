from abc import ABC, abstractclassmethod

from GameFiles.EngineScripts.HitBox import HitBox
from GameFiles.EngineScripts.Vector2 import Vector2


class GameObject(ABC):

	def __init__(self, game_display, color=(255, 255, 255)):
		self.lead_vertex = Vector2(0, 0)
		self.size = Vector2(5, 5)
		self.display = game_display
		self.color = color
		self.hitbox = None

	@abstractclassmethod
	def update(self):
		pass

	def render(self):
		self.display.fill(self.color, rect=[self.lead_vertex.x, self.lead_vertex.y, self.size.x, self.size.y])

	def hitbox_check(self, second_hitbox):
		if self.hitbox is not None and type(self.hitbox) == HitBox:
			return self.hitbox.got_hit(second_hitbox)
		else:
			return False

	@abstractclassmethod
	def on_enter(self, other_game_object):
		pass

	@abstractclassmethod
	def on_exit(self, other_game_object):
		pass
