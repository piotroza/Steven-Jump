import pygame

class Button:
    def __init__(self):
        self.price = 3
        self.level = 1
    sprite = pygame.image.load('assets/gfx/button2.png')
    typeIndicatorSprite = pygame.image.load('assets/gfx/null_indicator.png')
