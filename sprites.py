import pygame as pg
import random
from settings import *

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.player_img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

        self.health = PLAYER_HEALTH
        self.strength = PLAYER_STRENGTH
    
    def move(self, dx = 0, dy = 0):
        if not self.collide(dx * TILESIZE, dy * TILESIZE):
            self.x += dx * TILESIZE
            self.y += dy * TILESIZE

    def collide(self, dx = 0, dy = 0):
        for wall in self.game.walls:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                return True
        for mob in self.game.mobs:
            if mob.x == self.x + dx and mob.y == self.y + dy:
                mob.health -= self.strength
                return True
        for build in self.game.builds:
            if build.x == self.x + dx and build.y == self.y + dy:
                return True
        for tree in self.game.trees:
            if tree.x == self.x + dx and tree.y == self.y + dy:
                return True
        return False

    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y
        if self.health <= 0:
            self.kill()

class Mob(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.mobs
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.mob_img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

        self.health = MOB_HEALTH
        self.strength = MOB_STRENGTH

    def collide(self, dx = 0, dy = 0):
        for wall in self.game.walls:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                return True
        for mob in self.game.mobs:
            if mob.x == self.x + dx and mob.y == self.y + dy:
                return True
        for build in self.game.builds:
            if build.x == self.x + dx and build.y == self.y + dy:
                return True
        for tree in self.game.trees:
            if tree.x == self.x + dx and tree.y == self.y + dy:
                return True
        return False

    def collide_with_player(self, dx = 0, dy = 0):
        if self.game.player.x == self.x + dx and self.game.player.y == self.y + dy:
            self.game.player.health -= self.strength
            return True
        return False

    def move_toward(self):
        dx = self.game.player.x - self.x
        dy = self.game.player.y - self.y
        d = abs(dx) + abs(dy)
        if dy < 0:
            if not self.move(dy = -1):
                self.move(dx = random.randint(-1, 1))
        elif dx < 0:
            if not self.move(dx = -1):
                self.move(dy = random.randint(-1, 1))
        elif dy > 0:
            if not self.move(dy = 1):
                self.move(dx = random.randint(-1, 1))
        elif dx > 0:
            if not self.move(dx = 1):
                self.move(dy = random.randint(-1, 1))

    def move(self, dx = 0, dy = 0):
        if not self.collide(dx * TILESIZE, dy * TILESIZE) and not self.collide_with_player(dx * TILESIZE, dy * TILESIZE):
            self.x += dx * TILESIZE
            self.y += dy * TILESIZE
            return True
        return False

    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y
        if self.health <= 0:
            self.kill()

class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.wall_img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Obstacle(pg.sprite.Sprite):
    def __init__(self, game, x, y, w, h):
        self.groups = game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.rect = pg.Rect(x, y, w, h)
        self.x = x
        self.y = y