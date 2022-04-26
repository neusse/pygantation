import pygame
from code.initialization import *

def quit_window():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.mixer.music.stop()
            run = False
            pygame.display.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.mixer.music.stop()
                run = False
                pygame.display.quit()
                quit()
    clock.tick(60)
    pygame.display.update()
