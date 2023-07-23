import pygame
import singleton
from world import World
from config import init_config


def initialize():
    init_config()
    _init_display()
    _init_singleton()
    singleton.World = World(singleton.options['World']['size'])
    _init_freefont()


def _init_display():
    try:
        pygame.display.init()
        pygame.display.set_mode((800, 540))
        singleton.cell_size = 500 / singleton.options['World']['size']
    except Exception:
        exit(1)


def _init_singleton():
    singleton.cell_size = 500 / singleton.options['World']['size']
    singleton.World = World(singleton.options['World']['size'])
    singleton.world_timer = pygame.time.set_timer(pygame.USEREVENT, 1000)


def _init_freefont():
    pygame.freetype.init()
    singleton.font = pygame.freetype.Font("evil-empire.ttf", size=32)
