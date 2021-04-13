import pygame as pg
import random
from settings import *

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y, 
                 health = PLAYER_HEALTH, 
                 damage = PLAYER_DAMAGE, 
                 armor = PLAYER_ARMOR, 
                 weapon = 'weapon1', 
                 keys = 0, 
                 potions = 0, 
                 books = 0, 
                 health_upgrade = 0, 
                 armor_upgrade = 0,
                 moves = 0):
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

        try:
            self.weapon_img = game.item_images[weapon]
        except KeyError:
            self.weapon_img = weapon
        self.coins = int(self.game.data[0])
        self.level = 1
        self.health_upgrade = health_upgrade
        self.armor_upgrade = armor_upgrade
        self.health = health + (self.health_upgrade * 20) # ?
        self.damage = damage
        self.armor = armor + self.armor_upgrade # ?
        self.keys = keys
        self.potions = potions
        self.books = books
        self.moves = moves
    
    def move(self, dx = 0, dy = 0):
        if not self.collide(dx * TILESIZE, dy * TILESIZE):
            self.x += dx * TILESIZE
            self.y += dy * TILESIZE
            self.game.footstep.play()
            self.moves += 1

    def collide(self, dx = 0, dy = 0):
        for wall in self.game.walls:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                self.game.sound.play()
                return True
        for mob in self.game.mobs:
            if mob.x == self.x + dx and mob.y == self.y + dy:
                mob.health -= self.damage
                return True
        for chest in self.game.chests:
            if chest.x == self.x + dx and chest.y == self.y + dy:
                if self.keys > 0:
                    chest.kill()
                    self.random_item(self.game, chest.x, chest.y)
                    self.keys -= 1
                    return True
                self.game.sound.play()
                return True
        for sign in self.game.signs:
            if sign.x == self.x + dx and sign.y == self.y + dy:
                print(sign.text)
                self.game.sound.play()
                return True
        for travel in self.game.travels:
            if travel.x == self.x + dx and travel.y == self.y + dy:
                if travel.name == 'travel':
                    random_travel = random.choice(TRAVEL_LIST)
                    if random_travel == self.game.map_name[:-4]:
                        self.game.new(f'travel1.tmx', 
                                        self.health, 
                                        self.damage, 
                                        self.armor, 
                                        self.weapon_img, 
                                        self.keys, 
                                        self.potions, 
                                        self.books, 
                                        self.health_upgrade, 
                                        self.armor_upgrade, 
                                        self.moves)
                    else:
                        self.game.new(f'{random_travel}.tmx', 
                                        self.health, 
                                        self.damage, 
                                        self.armor, 
                                        self.weapon_img, 
                                        self.keys, 
                                        self.potions, 
                                        self.books, 
                                        self.health_upgrade, 
                                        self.armor_upgrade,
                                        self.moves)
                else:
                    self.game.new(f'{travel.name}.tmx', 
                                    self.health, self.damage, 
                                    self.armor, 
                                    self.weapon_img, 
                                    self.keys, 
                                    self.potions, 
                                    self.books, 
                                    self.health_upgrade, 
                                    self.armor_upgrade,
                                    self.moves)
                self.game.sound.play()
                self.game.run()
                return True
        return False

    def item_ontop(self, x, y):
        for item in self.game.items:
            if item.x == self.x and item.y == self.y:
                if item.type == 'heart' and self.health < PLAYER_HEALTH:
                    item.kill()
                    self.add_health(HEART_AMOUNT)
                if item.type == 'coin':
                    item.kill()
                    self.coins += 1
                if item.type == 'key':
                    item.kill()
                    self.keys += 1
                if item.type == 'potion':
                    item.kill()
                    self.potions += 1
                if item.type == 'book':
                    item.kill()
                    self.books += 1
                if item.type == 'weapon1':
                    item.kill()
                    self.better_damage(item.type, WEAPON1_AMOUNT)
                if item.type == 'weapon2':
                    item.kill()
                    self.better_damage(item.type, WEAPON2_AMOUNT)
                if item.type == 'weapon3':
                    item.kill()
                    self.better_damage(item.type, WEAPON3_AMOUNT)
                if item.type == 'weapon4':
                    item.kill()
                    self.better_damage(item.type, WEAPON4_AMOUNT)
                if item.type == 'weapon5':
                    item.kill()
                    self.better_damage(item.type, WEAPON5_AMOUNT)
                if item.type == 'weapon6':
                    item.kill()
                    self.better_damage(item.type, WEAPON6_AMOUNT)
                if item.type == 'weapon7':
                    item.kill()
                    self.better_damage(item.type, WEAPON7_AMOUNT)
                if item.type == 'weapon8':
                    item.kill()
                    self.better_damage(item.type, WEAPON8_AMOUNT)
                if item.type == 'armor1':
                    item.kill()
                    self.armor_amount(ARMOR1_AMOUNT)
                if item.type == 'armor2':
                    item.kill()
                    self.armor_amount(ARMOR2_AMOUNT)
                if item.type == 'armor3':
                    item.kill()
                    self.armor_amount(ARMOR3_AMOUNT)

    def random_item(self, game, x, y):
        item = random.choice(list(self.game.item_images))
        Item(self.game, x, y, item)

    def better_damage(self, img, amount):
        if self.damage < PLAYER_DAMAGE + amount:
            self.weapon_img = self.game.item_images[img]
            self.damage = PLAYER_DAMAGE + amount

    def armor_amount(self, amount):
        self.armor += amount
        if self.armor > PLAYER_ARMOR:
            self.armor = PLAYER_ARMOR

    def add_health(self, amount):
        self.health += amount
        if self.health > PLAYER_HEALTH:
            self.health = PLAYER_HEALTH

    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y
        if self.item_ontop(self.x, self.y):
            self.x += dx * TILESIZE
            self.y += dy * TILESIZE

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
        if self.type == 'mob4':
            self.health = MOB4_HEALTH
            self.damage = MOB4_DAMAGE

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
        for sign in self.game.signs:
            if sign.x == self.x + dx and sign.y == self.y + dy:
                return True
        for travel in self.game.travels:
            if travel.x == self.x + dx and travel.y == self.y + dy:
                return True
        return False

    def player_collide(self, dx = 0, dy = 0):
        if self.game.player.x == self.x + dx and self.game.player.y == self.y + dy:
            if self.game.player.armor > 0:
                self.game.player.armor -= 1
            else:
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

    def check_item(self, x, y):
        for item in self.game.items:
            if item.x == self.x and item.y == self.y:
                return True
        return False

    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y
        if self.health <= 0:
            self.kill()
            self.game.player.coins += 1
            rand = random.randint(1, 20)
            if rand == 1:
                Player.random_item(self, self.game, self.x, self.y)
            if not self.check_item(self.x, self.y):
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

class Sign(pg.sprite.Sprite):
    def __init__(self, game, x, y, text):
        self._layer = WALL_LAYER
        self.groups = game.all_sprites, game.signs
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.sign_img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y
        self.text = text

class Travel(pg.sprite.Sprite):
    def __init__(self, game, x, y, w, h, name):
        self.groups = game.travels
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.rect = pg.Rect(x, y, w, h)
        self.x = x
        self.y = y
        self.name = name