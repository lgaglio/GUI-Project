import math


class Vector2:
	@staticmethod
	def is_vector2( o ):
		if isinstance( o, Vector2 ):
			return True
		else:
			return False

	def __init__( self ):
		self.x = 0
		self.y = 0

	def distance( self, other_vector2 ):
		if not Vector2.is_vector2( other_vector2 ):
			raise TypeError

		return math.sqrt( math.pow( other_vector2.x - self.x, 2 ) + math.pow( other_vector2.y - self.y, 2 ) )


class Vector3( Vector2 ):
	@staticmethod
	def is_vector3( o ):
		if isinstance( o, Vector3 ):
			return True
		else:
			return False

	def __init__( self ):
		Vector2.__init__( self )
		self.z = 0

	def distance( self, other_vector3 ):
		if Vector3.is_vector2( other_vector3 ):
			result = math.sqrt( math.pow( other_vector3.x - self.x, 2 ) + math.pow( other_vector3.y - self.y, 2 ) + math.pow( 0 - self.z, 2 ) )
		elif Vector3.is_vector3( other_vector3 ):
			result = math.sqrt( math.pow( other_vector3.x - self.x, 2 )
			                    + math.pow( other_vector3.y - self.y, 2 )
			                    + math.pow( other_vector3.z - self.z, 2 ) )
		else:
			raise TypeError

		return result
