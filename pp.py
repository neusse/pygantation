import pygame
from code.quit_window import quit_window
from code.button import Button
from code.initialization import *
from code.label import *
from code.speaker import speak

# speak("La sicurezza sul lavoro", "it")
# Button 1 istance


# ============================= BUTTONS ACTIONS ======
def button_definition_action():
	''' button DEFINIZIONE '''
	global definition

	definition.change_text("Ascolta")
	x = speak(
		'''riguarda il poter svolgere il proprio lavoro
		in un ambiente in cui sia ridotto al minimo
		il rischio di infortunio e malattie professionali''',
		"it")
	print(x)

# ============== WIDGETS ISTANCES ========================
# Label
lb1 = Label(
	screen,
	text="Salute e sicurezza sul lavoro", 
	position=(0, 0),
	size=20,
	color="white")

definition = Button( # BUTTON DEFINIZIONE
	screen, 
	text="Definizione",
	position=(100, 100),
	size=40,
	color=(255,255,0),
	command=button_definition_action)


def main():
	while True:
		
		quit_window() # quit with the x
		definition.blit() # show button 1 definition
		labels_blit()
		pygame.display.update() 


main()
