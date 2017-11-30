# This game is being rewritten in Pygame. For install in PyCharm (I, TechNGamer, recommend) is to go to File -> Settings
#  -> Project: GUI Project -> Project Interpreter. Double click anywhere in the list box to open the package manager.
#  Search for pygame, and install the latest version. For my project team mates, follow this tutorial:
# https://www.youtube.com/watch?v=K5F-aGDIYaM&index=1&list=PL6gx4Cwl9DGAjkwJocj7vlc_mFU-4wXJq

import pygame
from EngineScripts.Frogger import *

status = pygame.init()

if status[1] > 0:
	print("Unsuccessful launch.")
	exit(-1)
else:
	print("Successful.")

game_display = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Frogger")

pygame.display.update()

exit_game = False

frog = Frogger()

objects = [frog]

while not exit_game:
	for event in pygame.event.get():
		print(event)

		if event.type == pygame.QUIT:
			exit_game = True

	pygame.display.update()

pygame.quit()
quit(0)
