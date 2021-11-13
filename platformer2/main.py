import pygame
import sys
from settings import *
from sprites import *

class Main:
    def __init__(self):
        pygame.init()
        self.running = True
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()

    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(60) / 1000
            self.draw()
            if not self.paused:
                self.update()
                self.events()

    def new(self):
        self.paused = False
        self.player = Player(self, 100, 100)
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)

    def quit(self):
        pygame.quit()
        sys.exit()

    def draw(self):
        pygame.display.set_caption("Platformer | FPS: {:.2f}".format(self.clock.get_fps()))
        self.screen.fill((0,0,0))
        self.all_sprites.draw(self.screen)
        pygame.display.flip()

    def update(self):
        pass

    def events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    m.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        m.quit()

m = Main()

while m.running:
    m.new()
    m.run()