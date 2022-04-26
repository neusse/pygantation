import pygame
from code.quit_window import quit_window
from code.button import *
from code.initialization import *
from code.label import *
from code.speaker import speak


b1 = Button(
    screen, 
    text="- Definizione",
    position=(0, 100),
    size=40,
    color=(255,255,0),
    command=lambda: speak('''Definizione: riguarda il poter svolgere il proprio lavoro
        in un ambiente in cui sia ridotto al minimo
        il rischio di infortunio e malattie professionali''',"it"))

b2 = Button(
    screen, 
    text="- Cosa bisogna proteggere?",
    position=(0, 150),
    size=40,
    color=(255,255,0),
    command=lambda: speak('''Bisogna proteggere: Il luogo di lavoro, le attrezzature e il corpo del lavoratore ''',"it"))

# Label
lb1 = Label(
    screen,
    text="Testo unico sulla salute e sicurezza sul lavoro", 
    position=(10, 0),
    size=60,
    color="white")

def main():
    while True:
        quit_window()
        b1.blit()
        b2.blit()
        labels_blit()
    pygame.display.flip()


main()
