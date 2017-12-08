# This game is being rewritten in Pygame. For install in PyCharm (I, TechNGamer, recommend) is to go to File -> Settings
#  -> Project: GUI Project -> Project Interpreter. Double click anywhere in the list box to open the package manager.
#  Search for pygame, and install the latest version. For my project team mates, follow this tutorial:
# https://www.youtube.com/watch?v=K5F-aGDIYaM&index=1&list=PL6gx4Cwl9DGAjkwJocj7vlc_mFU-4wXJq

from GameFiles.EngineScripts.Frogger import *


class Main:
	WHITE = (255, 255, 255)

	def __init__(self):

		status = pygame.init()

		if status[1] > 0:
			print("Unsuccessful launch.")
			exit(-1)
		else:
			print("Successful.")

		self.game_display = pygame.display.set_mode((800, 600))

		pygame.display.set_caption("Frogger")

		pygame.display.update()

		self.exit_game = False

		self.objects = [ContinueMover(self.game_display, 3, 50)]

		# noinspection PyTypeChecker
		self.objects.append(Frogger(self.game_display, self))

		self.event_list = []
		self.game_over = False

		self.font = pygame.font.SysFont(None, 25)

	def run(self):

		while not self.exit_game:
			self.event_list = []

			self.game_display.fill(self.WHITE)

			for event in pygame.event.get():
				# Checks to see if the player wants to quit out of the game.
				if event.type == pygame.QUIT:
					self.exit_game = True
				# Checks to see if that game over flag has been raised and the player pressed any key.
				elif self.game_over and event.type == pygame.KEYDOWN:
					# This is a massive hack for now.
					pygame.quit()

					new__main = Main()

					self.exit_game = True

					new__main.run()
					break
				# Creates a new list that hass all the events in it for other classes to use.
				else:
					self.event_list.append(event)
			# Checks to see if the game over flag has been raised. If not, proceed to update every object.
			if not self.game_over:
				for game_object in self.objects:
					game_object.update()


			# Checks to see if the game over flag has been raised and game exit hasn't
			elif self.game_over and not self.exit_game:
				screen_text = self.font.render("Game Over!\nPress any key to play again.", True, (0, 0, 0))
				self.game_display.blit(screen_text, [400, 300])

			# for game_object in self.objects[0:self.objects.__len__() - 1]:
			for game_object_index in range(0, (self.objects.__len__()-1)):
				if self.objects[game_object_index] != self.objects[-1] and self.objects[-1].hitbox_check( self.objects[game_object_index].hitbox ):
					self.objects[-1].on_enter( self.objects[game_object_index] )
			# Checks to see if the exit game flag has been raised. If not, proceed to update that display and update the Tme.deltaTime.
			if not self.exit_game:
				pygame.display.update()

				Time.update()

		pygame.quit()


if __name__ == '__main__':
	main_class = Main()

	main_class.run()

	quit(0)
