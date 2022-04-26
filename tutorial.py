import pygame
from code.button import *
from code.label import *
from code.initialization import *
from code.speaker import speak
from code.quit_window import quit_window


def defbt2():
    print("\n[b2]")
    print("Button 2 Clicked")
    speak('''Ciao''',"it")

b1 = Button(
    screen, 
    text="- Hello",
    position=(0, 100),
    size=40,
    color=(255,255,0),
    command=lambda: speak('''Hello''',"en"))

b2 = Button(
    screen, 
    text="- Ciao",
    position=(0, 150),
    size=40,
    color=(255,255,0),
    command=defbt2)

# Label
lb1 = Label(
    screen,
    text="Pypresenter: example n. 1", 
    position=(10, 0),
    size=60,
    color="white")

def main():
    while True:

        quit_window()
        b1.blit()
        b2.blit()
        labels_blit()




main()
