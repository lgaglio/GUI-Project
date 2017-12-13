import pygameimport GameFiles.EngineScripts.Data.Scripts.Time as Timefrom GameFiles.EngineScripts.Data.Objects.Moving.SelfMoving.ContinueMover import ContinueMoverfrom GameFiles.EngineScripts.Data.Objects.Moving.SelfMoving.Log import Logfrom GameFiles.EngineScripts.GameObject import GameObjectfrom GameFiles.EngineScripts.Data.Objects.HitBox import HitBoxfrom GameFiles.EngineScripts.Data.Objects.Vector2 import Vector2class Frogger(GameObject):	def __init__(self, game_display, main_class):		super().__init__(game_display)		# Vector2's		self.lead_vertex = Vector2(500, 500)		self.size = Vector2(20, 20)		self.difference = Vector2()		# Hitbox		self.hitbox = HitBox(self, self.lead_vertex, self.size)		# Main class		self.main_class_link = main_class		# Color		self.color = (0, 255, 0)		# Booleans		self.button_down = False		self.on_log = False		# Integers		self.speed = 100		self.direction = 0		self.log_speed = -1	def update(self):		if self.lead_vertex.y <= 0:			print("Victory!")			ContinueMover.inc_speed(20)			self.lead_vertex.y = 500		# Loops through the list of events that have happened.		for event in self.main_class_link.event_list:			if event.type == pygame.KEYDOWN:				if event.key == pygame.K_UP:					self.button_down = True					self.direction = 0				elif event.key == pygame.K_LEFT:					self.button_down = True					self.direction = 1				elif event.key == pygame.K_RIGHT:					self.button_down = True					self.direction = 2			elif event.type == pygame.KEYUP:				if event.key == pygame.K_UP or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:					self.button_down = False		# Checks to see if a button is down, and if so, to move Frogger in that direction.		if self.button_down:			if self.direction == 0:				self.lead_vertex.y -= self.speed * Time.deltaTime			elif self.direction == 1:				self.lead_vertex.x -= self.speed * Time.deltaTime			elif self.direction == 2:				self.lead_vertex.x += self.speed * Time.deltaTime		if self.on_log:			self.lead_vertex.x += self.log_speed * Time.deltaTime	def on_enter( self, other_game_object ):		if type(other_game_object) == ContinueMover:			self.on_log = True			difference = self.lead_vertex - other_game_object.lead_vertex			if difference.x > other_game_object.size.x - self.size.x:				self.main_class_link.game_over = True			elif difference.x < other_game_object.lead_vertex.x - self.size.x:				self.main_class_link.game_over = True			self.log_speed = ContinueMover.get_speed()	def on_exit( self, other_game_object ):		pass