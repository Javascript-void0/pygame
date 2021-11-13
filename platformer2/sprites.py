import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self.x = x
        self.y = y
        self.image = pygame.Surface((30, 40))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()

    def move():
        pass