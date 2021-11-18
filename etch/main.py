import sys
import pygame
from pygame import gfxdraw

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen_color = (255, 255, 255)
screen.fill(screen_color)
pygame.display.flip()

penX, penY = 0, 0
pen_color = (0, 0, 0)
gfxdraw.pixel(screen, penX, penY, pen_color)
pygame.display.flip()
pygame.display.set_caption('Etch A Sketch')
pygame.key.set_repeat(200, 20)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_ESCAPE]:
                pygame.quit()
                sys.exit()
            if pressed[pygame.K_SPACE]:
                screen.fill(screen_color)
                pygame.display.flip()
            if pressed[pygame.K_UP]:
                if penY - 1 != -1:
                    penY -= 1
            if pressed[pygame.K_DOWN]:
                if penY + 1 != HEIGHT + 1:
                    penY += 1
            if pressed[pygame.K_LEFT]:
                if penX - 1 != -1:
                    penX -= 1
            if pressed[pygame.K_RIGHT]:
                if penX + 1 != WIDTH + 1:
                    penX += 1
            gfxdraw.pixel(screen, penX, penY, pen_color)
            pygame.display.flip()