import pygame
import singleton


def shutdown():
    singleton.display = None
    pygame.display.quit()
