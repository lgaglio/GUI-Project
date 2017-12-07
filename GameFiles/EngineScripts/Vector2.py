class Vector2:

	def __init__(self, x = 0, y = 0):
		if not (type(x) == int or type(x) == float or type(y) == int or type(y) == float):
			raise TypeError("Data type does not match what was expected.")
		else:
			self.x = x
			self.y = y
