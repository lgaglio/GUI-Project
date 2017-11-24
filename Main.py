# noinspection PyCompatibility
import tkinter as Tkinter
from Components.Log import Log

# Variables that are to be used.
logs = []
score = 0

root = Tkinter.Tk() # Starts a new Tkinter window.

root.resizable(0,0) # Disables resizing of the window.

root.wm_title( 'Basic Frogger v0.2.5' ) # Gives a name to the tkinter window.

# Execute operations.
score_text = Tkinter.Label( root, text = 'Score: %d' % score )
lives_text = Tkinter.Label(root, text = 'Lives: 3' )

# Places the text on the window
score_text.grid( row = 0, column = 1 )
lives_text.grid( row = 0, column = 2 )

# Where the game will be made on.
canvas = Tkinter.Canvas( root, width = 800, height = 600, background = '#006200' )
canvas.grid( row = 1, rowspan = 4, column = 0, columnspan = 4 )

water = canvas.create_rectangle( -10, 20, 900, 170, outline = '#DBB84D', fill = '#00E6E6' ) # Creates the water background.

road = canvas.create_rectangle( -10, 230, 900, 440, fill = '#000000' ) # Creates the road background.

shoreLine = canvas.create_rectangle( -10, 170, 900, 230, outline = '#DBB84D', fill = '#DBB84D' ) # Creates the shoreline background.

# Set's them to the lower part of the background.
canvas.lower( shoreLine )
canvas.lower( water )

while root.:



root.mainloop()
