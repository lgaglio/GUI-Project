from GameFiles.EngineScripts.Vector2 import Vector2


class HitBox:

	def __init__(self, parent_game_object, vertex1, vertex2):
		if type(vertex1) != Vector2:
			raise TypeError("Expected Vector2, but got %s" % type(vertex1))
		elif type(vertex2) != Vector2:
			raise TypeError("Expected Vector2, but got %s" % type(vertex2))
		else:
			self.game_object = parent_game_object
			self.vertex1 = vertex1
			self.vertex2 = vertex2

	def got_hit(self, second_hitbox):
		if type(second_hitbox) != HitBox:
			raise TypeError("Expected hitbox, but got %s" % type(second_hitbox))

		in_between_x = False
		in_between_y = False

		# TODO: Complete collision check.
		if second_hitbox.vertex1.x < self.vertex1.x < second_hitbox.vertex1.x + second_hitbox.vertex2.x \
				or second_hitbox.vertex1.x < self.vertex1.x + self.vertex2.x < second_hitbox.vertex1.x + second_hitbox.vertex2.x:
			in_between_x = True

		if second_hitbox.vertex1.y < self.vertex1.y < second_hitbox.vertex1.y + second_hitbox.vertex2.y \
				or second_hitbox.vertex1.y < self.vertex1.y + self.vertex2.y < second_hitbox.vertex1.y + second_hitbox.vertex2.y:
			in_between_y = True

		if in_between_x and in_between_y:
			return True
		else:
			return False
