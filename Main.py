'''Any notes shall go in the space below.
Add Easter Eggs and Secrets
'''
from __future__ import print_function

import random as r

import Tkinter

# This creates the window that will hold it.
root = Tkinter.Tk()
root.wm_title( 'Basic Frogger v0.2.5' )
# This is where the global variables will be located
debuggerAchivement = False
logs0 = []
logs1 = []
logs2 = []
logs3 = []
logs4 = []
cars0 = []
cars1 = []
cars2 = []
cars3 = []
cars4 = []
score = 0
velocity_xcars = 0
velocity_xlogs = 0
allowMovement1 = True
allowMovement2 = True
allowMovement3 = True
debuggerOn = False
pauseOn = False
Game_Over = ''
LineN = 1
text = Tkinter.Label( root, text = 'Score: ' + str( score ) )
frogger = []
lives = 3
currentmode = Tkinter.IntVar()
liveText = Tkinter.Label( root, text = 'Lives: ' + str( lives ) )
# Places it on the window
text.grid( row = 0, column = 3 )
liveText.grid( row = 0, column = 4 )
# Sets current mode
currentmode.set( 0 )
# These are the buttons that will be dsplayed at the top
easybutton = Tkinter.Radiobutton( root, text = 'Easy', variable = currentmode, value = 0 )
mediumbutton = Tkinter.Radiobutton( root, text = 'Medium', variable = currentmode, value = 1 )
hardbutton = Tkinter.Radiobutton( root, text = 'Hard', variable = currentmode, value = 2 )
easybutton.grid( row = 0, column = 0 )
mediumbutton.grid( row = 0, column = 1 )
hardbutton.grid( row = 0, column = 2 )
# This is the canvas where the game will be displayed at
canvas = Tkinter.Canvas( root, width = 800, height = 600, background = '#006200' )
canvas.grid( row = 1, rowspan = 4, column = 0, columnspan = 5 )
water = canvas.create_rectangle( -10, 20, 900, 170, outline = '#DBB84D', fill = '#00E6E6' )
road = canvas.create_rectangle( -10, 230, 900, 440, fill = '#000000' )
shoreLine = canvas.create_rectangle( -10, 170, 900, 230, outline = '#DBB84D', fill = '#DBB84D' )
canvas.lower( shoreLine )
canvas.lower( water )


# Spawns in the logs
def logs( startX, startY, row ):
	global logs0, logs1, logs2, logs3, logs4
	if row == 0:
		logs0 = canvas.create_rectangle( startX, startY, startX + 199, startY + 30, outline = '#000000', fill = '#663300' )
		canvas.lower( logs0 )
	elif row == 1:
		logs1 = canvas.create_rectangle( startX, startY + 30, startX - 199, startY + 60, outline = '#000000', fill = '#663300' )
		canvas.lower( logs1 )
	elif row == 2:
		logs2 = canvas.create_rectangle( startX, startY + 60, startX + 199, startY + 90, outline = '#000000', fill = '#663300' )
		canvas.lower( logs2 )
	elif row == 3:
		logs3 = canvas.create_rectangle( startX, startY + 90, startX - 199, startY + 120, outline = '#000000', fill = '#663300' )
		canvas.lower( logs3 )
	else:
		logs4 = canvas.create_rectangle( startX, startY + 120, startX + 199, startY + 150, outline = '#000000', fill = '#663300' )
		canvas.lower( logs4 )
	canvas.lower( water )


# Spawns in the cars
def cars( startX, startY, row ):
	global cars0, cars1, cars2, cars3, cars4
	if row == 0:
		cars0 = + canvas.create_rectangle( startX - 30, startY + 110, startX, startY + 135, outline = '#000099', fill = '#000099' )
	elif row == 1:
		cars1 = + canvas.create_rectangle( startX - 30, startY + 143, startX, startY + 165, outline = '#FFFF00', fill = '#FFFF00' )
	elif row == 2:
		cars2 = + canvas.create_rectangle( startX - 30, startY + 172, startX, startY + 195, outline = '#FF0000', fill = '#FF0000' )
	elif row == 3:
		cars3 = + canvas.create_rectangle( startX - 30, startY + 202, startX, startY + 225, outline = '#FFFFFF', fill = '#FFFFFF' )
	else:
		cars4 = + canvas.create_rectangle( startX - 30, startY + 235, startX, startY + 258, outline = '#000000', fill = '#0099FF' )


# Where most of the calculations are made
def Game_core():
	startX1 = -200
	startY1 = 20
	startX2 = 1000
	startY2 = 150
	spawner = r.randint( 0, 1 )
	if spawner == 1:
		x1, y1, x2, y2 = canvas.coords( logs0 )
		x3, y3, x4, y4 = canvas.coords( logs1 )
		x5, y5, x6, y6 = canvas.coords( logs2 )
		x7, y7, x8, y8 = canvas.coords( logs3 )
		x9, y9, x10, y10 = canvas.coords( logs4 )
		x11, y11, x12, y12 = canvas.coords( cars0 )
		x13, y13, x14, y14 = canvas.coords( cars1 )
		x15, y15, x16, y16 = canvas.coords( cars2 )
		x17, y17, x18, y18 = canvas.coords( cars3 )
		x19, y19, x20, y20 = canvas.coords( cars4 )
		if x1 > 810:
			global startX1, startY1
			logs( startX1, startY1, 0 )
		if x4 < 0:
			global startX2, startY1
			logs( startX2, startY1, 1 )
		if x5 > 810:
			global startX1, startY1
			logs( startX1, startY1, 2 )
		if x8 < 0:
			global startX2, startY1
			logs( startX2, startY1, 3 )
		if x9 > 810:
			global startX1, startY1
			logs( startX1, startY1, 4 )
		if x12 < 0:
			global startX2, startY2
			cars( startX2, startY2, 0 )
		if x13 > 810:
			global startX1, startY2
			cars( startX1, startY2, 1 )
		if x16 < 0:
			global startX2, startY2
			cars( startX2, startY2, 2 )
		if x17 > 810:
			global startX1, startY2
			cars( startX1, startY2, 3 )
		if x20 < 0:
			global startX2, startY2
			cars( startX2, startY2, 4 )


# Checks to see if you continue, die, or win
def Win_or_Death():
	global frogger, score
	x1, y1, x2, y2 = canvas.coords( logs0 )
	x3, y3, x4, y4 = canvas.coords( logs1 )
	x5, y5, x6, y6 = canvas.coords( logs2 )
	x7, y7, x8, y8 = canvas.coords( logs3 )
	x9, y9, x10, y10 = canvas.coords( logs4 )
	x11, y11, x12, y12 = canvas.coords( cars0 )
	x13, y13, x14, y14 = canvas.coords( cars1 )
	x15, y15, x16, y16 = canvas.coords( cars2 )
	x17, y17, x18, y18 = canvas.coords( cars3 )
	x19, y19, x20, y20 = canvas.coords( cars4 )
	x21, y21, x22, y22 = canvas.coords( frogger )
	if debuggerOn == True:
		print( 'Log 1: X1: ', x1, ' Y1: ', y1, ' X2: ', x2, ' Y2: ', y2 )
		print( 'Log 2: X1: ', x3, ' Y1: ', y3, ' X2: ', x4, ' Y2: ', y4 )
		print( 'Log 3: X1: ', x5, ' Y1: ', y5, ' X2: ', x6, ' Y2: ', y6 )
		print( 'Log 4: X1: ', x7, ' Y1: ', y7, ' X2: ', x8, ' Y2: ', y8 )
		print( 'Log 5: X1: ', x9, ' Y1: ', y9, ' X2: ', x10, ' Y2: ', y10 )
		print( 'Car 1: X1: ', x11, ' Y1: ', y11, ' X2: ', x12, ' Y2: ', y12 )
		print( 'Car 2: X1: ', x13, ' Y1: ', y13, ' X2: ', x14, ' Y2: ', y14 )
		print( 'Car 3: X1: ', x15, ' Y1: ', y15, ' X2: ', x16, ' Y2: ', y16 )
		print( 'Car 4: X1: ', x17, ' Y1: ', y17, ' X2: ', x18, ' Y2: ', y18 )
		print( 'Car 5: X1: ', x19, ' Y1: ', y19, ' X2: ', x20, ' Y2: ', y20 )
		print( 'Frogger: X1: ', x21, ' Y1: ', y21, ' X2: ', x22, ' Y2: ', y22 )
		print( 'Allow Movement left: ', allowMovement1 )
		print( 'Allow Movement right: ', allowMovement2 )
		print( 'Allow Movement back: ', allowMovement3 )
		print( 'Acceleration on X axis: ', velocity_xlogs, velocity_xcars )
	if y22 <= 0:
		frogger = canvas.create_rectangle( 385, 590, 415, 560, outline = '#000000', fill = '#75A319', tag = 'frogger' )
		score += 1
		text.config( text = 'Score: ' + str( score ) )
	elif x21 <= 5:
		global allowMovement1
		allowMovement1 = False
	elif x22 == 805:
		global allowMovement2
		allowMovement2 = False
	elif y22 >= 590:
		global allowMovement3
		allowMovement3 = False
	else:
		global allowMovement1, allowMovement2, allowMovement3
		allowMovement1 = True
		allowMovement2 = True
		allowMovement3 = True
	if y21 == 260:
		if x21 < x11 < x22:
			Death()
	if y21 == 290:
		if x21 < x14 < x22:
			Death()
	if y21 == 320:
		if x21 < x15 < x22:
			Death()
	if y21 == 350:
		if x21 < x18 < x22:
			Death()
	if y21 == 380:
		if x21 < x19 < x22:
			Death()
	if x22 <= 0 or x21 >= 800:
		Death()
	if y22 > 600:
		Death()


# Test whether in water or not
def onLogs():
	global frogger, score
	x1, y1, x2, y2 = canvas.coords( logs0 )
	x3, y3, x4, y4 = canvas.coords( logs1 )
	x5, y5, x6, y6 = canvas.coords( logs2 )
	x7, y7, x8, y8 = canvas.coords( logs3 )
	x9, y9, x10, y10 = canvas.coords( logs4 )
	x21, y21, x22, y22 = canvas.coords( frogger )
	if y21 < 170 and y22 > 20:
		onlog = False
		if x21 >= x1 and x22 <= x2:
			if y21 == y1 and y22 == y2:
				onlog = True
				canvas.move( frogger, velocity_xlogs + 1, 0 )
		if x21 >= x3 and x22 <= x4:
			if y21 == y3 and y22 == y4:
				onlog = True
				canvas.move( frogger, velocity_xlogs * -1, 0 )
		if x21 >= x5 and x22 <= x6:
			if y21 == y5 and y22 == y6:
				onlog = True
				canvas.move( frogger, velocity_xlogs - 1, 0 )
		if x21 >= x7 and x22 <= x8:
			if y21 == y7 and y22 == y8:
				onlog = True
				canvas.move( frogger, velocity_xlogs * -1.1, 0 )
		if x21 >= x9 and x22 <= x10:
			if y21 == y9 and y22 == y10:
				onlog = True
				canvas.move( frogger, velocity_xlogs, 0 )
				if debuggerOn == True:
					print( velocity_xlogs )
		if onlog == False:
			Death()


# Grants a key to kill frogger
def DeathTrans( event ):
	global lives
	lives = 1
	Death()


# Kills frogger and respawns him
def Death():
	global frogger, lives, score, Game_Over
	canvas.delete( frogger )
	frogger = canvas.create_rectangle( 385, 590, 415, 560, outline = '#000000', fill = '#75A319', tag = 'frogger' )
	lives = lives - 1
	if lives == 0:
		score = 0
		text.config( text = 'Score: ' + str( score ) )
		lives = 3
		Game_Over = canvas.create_text( 415, 300, text = 'Game Over', fill = '#FFFFFF', font = ('Arial', 40) )
		root.unbind( '<w>' )
		root.unbind( '<W>' )
		canvas.after( 10000, del_text )
	liveText.config( text = 'Lives: ' + str( lives ) )


def del_text():
	canvas.delete( Game_Over )


# Allows a key to skip to a new frame
def animateEvent( event ):
	animate()


# Moves all the items but Frogger
def animate():
	global velocity_xcars, velocity_xlogs
	if currentmode.get() == 0:
		velocity_xcars = 10
		velocity_xlogs = 7
	elif currentmode.get() == 1:
		velocity_xcars = 20
		velocity_xlogs = 8
	else:
		velocity_xcars = 30
		velocity_xlogs = 9
	velocity_y = 0
	# Change the canvas item's coordinates
	canvas.move( logs0, velocity_xlogs + 1, velocity_y )
	canvas.move( logs1, velocity_xlogs * -1, velocity_y )
	canvas.move( logs2, velocity_xlogs - 1, velocity_y )
	canvas.move( logs3, velocity_xlogs * -1.1, velocity_y )
	canvas.move( logs4, velocity_xlogs, velocity_y )
	canvas.move( cars0, (velocity_xcars - 1) * -1, velocity_y )
	canvas.move( cars1, velocity_xcars - 1, velocity_y )
	canvas.move( cars2, (velocity_xcars + 1) * -1, velocity_y )
	canvas.move( cars3, velocity_xcars + 1, velocity_y )
	canvas.move( cars4, velocity_xcars * -1, velocity_y )
	Game_core()
	Win_or_Death()
	onLogs()
	if (debuggerOn != True) and (pauseOn != True):
		canvas.after( 1, animate )


# Spawns and put everything in motion
cars( 800, 150, 0 )
cars( -6, 150, 1 )
cars( 800, 150, 2 )
cars( -6, 150, 3 )
cars( 800, 150, 4 )
logs( 1, 20, 0 )
logs( 800, 20, 1 )
logs( 1, 20, 2 )
logs( 800, 20, 3 )
logs( 1, 20, 4 )
frogger = canvas.create_rectangle( 385, 590, 415, 560, outline = '#000000', fill = '#75A319', tag = 'frogger' )
animate()


# Debugger
def moreLives( event ):
	global lives
	lives = lives + 3
	liveText.config( text = 'Lives: ' + str( lives ) )


def Frogger_up( event ):
	canvas.move( frogger, 0, -30 )


def Frogger_left( event ):
	if allowMovement1 == True:
		canvas.move( frogger, -30, 0 )


def Frogger_right( event ):
	if allowMovement2 == True:
		canvas.move( frogger, 30, 0 )


def Frogger_back( event ):
	if allowMovement3 == True:
		canvas.move( frogger, 0, 30 )


def Debuger_Once( event ):
	global debuggerAchivement, debuggerOn, lives
	if debuggerAchivement == False:
		achivement = Tkinter.Tk()
		achivement.wm_title( 'Achivement Unlocked' )
		achevementMessage = Tkinter.Label( achivement, text = 'You have discovered the debugger,\nCheater!' )
		achevementMessage.grid( column = 0, row = 0 )
		debuggerAchivement = True
		debug_Window()
	if debuggerOn != True:
		root.unbind( "<space>" )
	root.bind( "<F>", animateEvent )
	if score == 0:
		root.bind( "<L>", moreLives )
	root.bind( "<K>", DeathTrans )
	debuggerOn = True
	print( 'You have now entered debug mode.\nTo exit press B again.' )
	print( 'Extra controls in Debug Mode: F to skip to the next Frame and coords of EngineComponents.\nL for more lives.\nK for instant death' )


def Pause( event ):
	global pauseOn
	if pauseOn != True:
		pauseOn = True
		root.bind( "<w>" )
		root.bind( "<W>" )
		root.bind( "<a>" )
		root.bind( "<A>" )
		root.bind( "<d>" )
		root.bind( "<D>" )
		root.bind( "<B>" )
	else:
		root.unbind( "<w>" )
		root.unbind( "<W>" )
		root.unbind( "<a>" )
		root.unbind( "<A>" )
		root.unbind( "<d>" )
		root.unbind( "<D>" )
		root.unbind( "<B>" )
		pauseOn = False
		animate()


def debug_Window():
	debugWindow = Tkinter.Tk()
	debugWindow.wm_title( 'Debugger' )

	def Live():
		global lineN
		x1, y1, x2, y2 = canvas.coords( logs0 )
		x3, y3, x4, y4 = canvas.coords( logs1 )
		x5, y5, x6, y6 = canvas.coords( logs2 )
		x7, y7, x8, y8 = canvas.coords( logs3 )
		x9, y9, x10, y10 = canvas.coords( logs4 )
		x11, y11, x12, y12 = canvas.coords( cars0 )
		x13, y13, x14, y14 = canvas.coords( cars1 )
		x15, y15, x16, y16 = canvas.coords( cars2 )
		x17, y17, x18, y18 = canvas.coords( cars3 )
		x19, y19, x20, y20 = canvas.coords( cars4 )
		x21, y21, x22, y22 = canvas.coords( frogger )
		line1 = 'Log 1: X1: ' + str( x1 ) + ' Y1: ' + str( y1 ) + ' X2: ' + str( x2 ) + ' Y2: ' + str( y2 ) + '\n'
		line2 = 'Log 2: X1: ' + str( x3 ) + ' Y1: ' + str( y3 ) + ' X2: ' + str( x4 ) + ' Y2: ' + str( y4 ) + '\n'
		line3 = 'Log 3: X1: ' + str( x5 ) + ' Y1: ' + str( y5 ) + ' X2: ' + str( x6 ) + ' Y2: ' + str( y6 ) + '\n'
		line4 = 'Log 4: X1: ' + str( x7 ) + ' Y1: ' + str( y7 ) + ' X2: ' + str( x8 ) + ' Y2: ' + str( y8 ) + '\n'
		line5 = 'Log 5: X1: ' + str( x9 ) + ' Y1: ' + str( y9 ) + ' X2: ' + str( x10 ) + ' Y2: ' + str( y10 ) + '\n'
		line6 = 'Car 1: X1: ' + str( x11 ) + ' Y1: ' + str( y11 ) + ' X2: ' + str( x12 ) + ' Y2: ' + str( y12 ) + '\n'
		line7 = 'Car 2: X1: ' + str( x13 ) + ' Y1: ' + str( y13 ) + ' X2: ' + str( x14 ) + ' Y2: ' + str( y14 ) + '\n'
		line8 = 'Car 3: X1: ' + str( x15 ) + ' Y1: ' + str( y15 ) + ' X2: ' + str( x16 ) + ' Y2: ' + str( y16 ) + '\n'
		line9 = 'Car 4: X1: ' + str( x17 ) + ' Y1: ' + str( y17 ) + ' X2: ' + str( x18 ) + ' Y2: ' + str( y18 ) + '\n'
		line10 = 'Car 5: X1: ' + str( x19 ) + ' Y1: ' + str( y19 ) + ' X2: ' + str( x20 ) + ' Y2: ' + str( y20 ) + '\n'
		line11 = 'Frogger: X1: ' + str( x21 ) + ' Y1: ' + str( y21 ) + ' X2: ' + str( x22 ) + ' Y2: ' + str( y22 ) + '\n'
		line12 = 'Allow Movement left: ' + str( allowMovement1 ) + '\n'
		line13 = 'Allow Movement right: ' + str( allowMovement2 ) + '\n'
		line14 = 'Allow Movement back: ' + str( allowMovement3 ) + '\n'
		line15 = 'Acceleration on X axis: ' + str( velocity_xlogs ) + ' ' + str( velocity_xcars ) + '\n'
		if lineN != 16:
			text = Tkinter.label( debugWindow )
			lineNum = 'line' + str( lineN )
			text.insert( lineNum )
		canvas.after( 1, Live )


root.bind( "<w>", Frogger_up )
root.bind( "<W>", Frogger_up )
root.bind( "<a>", Frogger_left )
root.bind( "<A>", Frogger_left )
root.bind( "<d>", Frogger_right )
root.bind( "<D>", Frogger_right )
root.bind( "<s>", Frogger_back )
root.bind( "<S>", Frogger_back )
root.bind( "<B>", Debuger_Once )
root.bind( "<space>", Pause )
root.bind( "<Up>", Frogger_up )
root.bind( "<Left>", Frogger_left )
root.bind( "<Right>", Frogger_right )
root.mainloop()
