# This game is being rewritten in Pygame. For install in PyCharm (I, TechNGamer, recommend) is to go to File -> Settings
#  -> Project: GUI Project -> Project Interpreter. Double click anywhere in the list box to open the package manager.
#  Search for pygame, and install the latest version. For my project team mates, follow this tutorial:
# https://www.youtube.com/watch?v=K5F-aGDIYaM&index=1&list=PL6gx4Cwl9DGAjkwJocj7vlc_mFU-4wXJq

from GameFiles.EngineScripts.ContinueMover import *
from GameFiles.EngineScripts.Frogger import *

WHITE = (255, 255, 255)

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

frogger = Frogger(game_display)

objects = [ContinueMover(game_display, 1, 50)]

while not exit_game:

	game_display.fill(WHITE)

	event_list = []

	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			exit_game = True
		else:
			event_list.append(event)

	frogger.update(event_list)

	for game_object in objects:
		game_object.update()

	pygame.display.update()

	Time.update()

pygame.quit()
quit(0)
