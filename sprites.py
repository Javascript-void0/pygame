import pygame as pg
import random
from settings import *

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self._layer = PLAYER_LAYER
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.player_img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = self.x
        self.rect.y = self.y

        self.health = PLAYER_HEALTH
        self.damage = PLAYER_DAMAGE
        self.weapon_img = game.item_images['weapon1']
    
    def move(self, dx = 0, dy = 0):
        if self.item_collide(dx * TILESIZE, dy * TILESIZE):
            self.x += dx * TILESIZE
            self.y += dy * TILESIZE
        if not self.collide(dx * TILESIZE, dy * TILESIZE):
            if not self.chest_collide(dx * TILESIZE, dy * TILESIZE):
                self.x += dx * TILESIZE
                self.y += dy * TILESIZE

    def collide(self, dx = 0, dy = 0):
        for wall in self.game.walls:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                return True
        for mob in self.game.mobs:
            if mob.x == self.x + dx and mob.y == self.y + dy:
                mob.health -= self.damage
                return True
        return False

    def item_collide(self, dx = 0, dy = 0):
        for item in self.game.items:
            if item.x == self.x + dx and item.y == self.y + dy:
                if item.type == 'heart' and self.health < PLAYER_HEALTH:
                    item.kill()
                    self.add_health(HEART_AMOUNT)
                if item.type == 'weapon1':
                    item.kill()
                    self.weapon_img = self.game.item_images['weapon1']
                    if self.damage < PLAYER_DAMAGE + WEAPON1_AMOUNT:
                        self.add_damage(WEAPON1_AMOUNT)
                if item.type == 'weapon2':
                    item.kill()
                    self.weapon_img = self.game.item_images['weapon2']
                    if self.damage < PLAYER_DAMAGE + WEAPON2_AMOUNT:
                        self.add_damage(WEAPON2_AMOUNT)

    def chest_collide(self, dx = 0, dy = 0):
        for chest in self.game.chests:
            if chest.x == self.x + dx and chest.y == self.y + dy:
                chest.kill()
                self.random_item(self.game, chest.x, chest.y)
                return True
        return False

    def random_item(self, game, x, y):
        item = random.choice(list(self.game.item_images))
        Item(self.game, x, y, item)

    def add_damage(self, amount):
        self.damage = PLAYER_DAMAGE + amount

    def add_health(self, amount):
        self.health += amount
        if self.health > PLAYER_HEALTH:
            self.health = PLAYER_HEALTH

    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y

class Mob(pg.sprite.Sprite):
    def __init__(self, game, x, y, type):
        self._layer = MOB_LAYER
        self.groups = game.all_sprites, game.mobs
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.mob_images[type]
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y
        self.type = type

        if self.type == 'mob1':
            self.health = MOB1_HEALTH
            self.damage = MOB1_DAMAGE
        if self.type == 'mob2':
            self.health = MOB2_HEALTH
            self.damage = MOB2_DAMAGE
        if self.type == 'mob3':
            self.health = MOB3_HEALTH
            self.damage = MOB3_DAMAGE

    def collide(self, dx = 0, dy = 0):
        for wall in self.game.walls:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                return True
        for chest in self.game.chests:
            if chest.x == self.x + dx and chest.y == self.y + dy:
                return True
        for mob in self.game.mobs:
            if mob.x == self.x + dx and mob.y == self.y + dy:
                return True
        return False

    def player_collide(self, dx = 0, dy = 0):
        if self.game.player.x == self.x + dx and self.game.player.y == self.y + dy:
            self.game.player.health -= self.damage
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
        if not self.collide(dx * TILESIZE, dy * TILESIZE) and not self.player_collide(dx * TILESIZE, dy * TILESIZE):
            self.x += dx * TILESIZE
            self.y += dy * TILESIZE
            return True
        return False

    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y
        if self.health <= 0:
            self.kill()
            self.game.map_img.blit(self.game.skull_img, (self.x, self.y))

class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.wall_img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y

class Obstacle(pg.sprite.Sprite):
    def __init__(self, game, x, y, w, h):
        self.groups = game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.rect = pg.Rect(x, y, w, h)
        self.x = x
        self.y = y

class Item(pg.sprite.Sprite):
    def __init__(self, game, x, y, type):
        self._layer = ITEMS_LAYER
        self.groups = game.all_sprites, game.items
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.item_images[type]
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y
        self.type = type

class Chest(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self._layer = PLAYER_LAYER
        self.groups = game.all_sprites, game.chests
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.chest_img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y