import pygame


class Bone: 
    def __init__(self):
        self.sprite = pygame.image.load('assets/gfx/bone.png')
        self.position = pygame.Vector2()
        self.position.xy