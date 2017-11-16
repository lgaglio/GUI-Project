import EngineComponents.gameobject
import EngineComponents.vector


class Hitbox2D:

	def __init__(self, game_object):
		if isinstance(game_object, EngineComponents.gameobject.GameObject):
			attachedGameObject = game_object
