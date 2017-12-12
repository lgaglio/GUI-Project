class Vector2:

	def __init__(self, x=0, y=0):
		if not (type(x) == int or type(x) == float or type(y) == int or type(y) == float):
			raise TypeError("Data type does not match what was expected.")
		else:
			self.x = x
			self.y = y

	def distance(self, other):
		self.check_for_same(other)

		under_radican = pow(other.x - self.x, 2) + pow(other.y - self.y, 2)

		return pow(under_radican, 1 / 2)

	def __sub__(self, other):
		self.check_for_same(other)

		x = self.x - other.x
		y = self.y - other.y

		return Vector2(x, y)

	def __add__(self, other):
		self.check_for_same(other)

		x = self.x + other.x
		y = self.y + other.y

		return Vector2(x, y)

	def __mul__(self, other):
		self.check_for_same(other)

		x = self.x * other.x
		y = self.y * other.y

		return Vector2(x, y)

	def __truediv__(self, other):
		self.check_for_same(other)

		x = self.x / other.x
		y = self.y / other.y

		return Vector2(x, y)

	def __eq__(self, other):
		self.check_for_same(other)

		if self.x == other.x and self.y == other.y:
			return True
		else:
			return False

	def check_for_same(self, other):
		if type(other) != Vector2:
			raise TypeError("Expected Vector2.")
