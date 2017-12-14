from GameFiles.EngineScripts.GameObject import GameObject
from GameFiles.EngineScripts.Data.Objects.Moving.SelfMoving.ContinueMover import ContinueMover

class Log(ContinueMover):

	def __init__(self, game_display, direction, position):
		super().__init__(game_display, direction, 50, (140, 77, 0))

		self.lead_vertex = position
