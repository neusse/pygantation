
PYGAME WIDGETS REPOSITORY ON FORMAZIONE

WIDGETS for the presentation (usable for other scripts too)
=============================


BUTTONS
==============================================
# To create a button you give the screen as the main display surface,
# the text, the position, size, color and command




# Button 1 istance
b1 = Button(
	screen, 
	text="Hello",
	position=(100, 100),
	size=40,
	color=(255,255,0),
	command=lambda: print("hello"))

then you call it in the while True loop in the main file with

b1.blit() and you're done


LABELS
==============================================
lb1 = Label(
	screen,
	text="pythonprogramming.altervista.org", 
	position=(50, 360),
	size=20,
	color="white")
