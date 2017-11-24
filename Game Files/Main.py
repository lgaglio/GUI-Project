# This game is being rewritten in Pygame. For install in PyCharm (I, TechNGamer, recommend) is to go to File -> Settings -> Project: GUI Project -> Project
# Interpreter. Double click anywhere in the list box to open the package manager. Search for pygame, and install the latest version. For my project team mates,
# follow this tutorial: https://www.youtube.com/watch?v=K5F-aGDIYaM&index=1&list=PL6gx4Cwl9DGAjkwJocj7vlc_mFU-4wXJq

import pygame

status = pygame.init()

if status[1] > 0:
	print("Unsuccessful launch.")
	exit(-1)
else:
	print("Successful.")

gameDisplay = pygame.display.set_mode((800,600))

pygame.display.set_caption("Frogger")

pygame.display.update()



pygame.quit()
quit(0)
