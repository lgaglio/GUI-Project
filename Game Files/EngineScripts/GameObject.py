from abc import ABC, abstractclassmethod


class GameObject(ABC):

	@abstractclassmethod
	def __init__(self):
		self.vector2 = [0, 0]

	@abstractclassmethod
	def update(self):
		pass
