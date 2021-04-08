import pygame as pg
import sys
import random
from os import path
from settings import *
from sprites import *
from tilemap import *

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.running = True
        pg.key.set_repeat(200, 100)
        self.load_data()

    def draw_text(self, text, font_name, size, color, x, y, align="nw"):
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        if align == "nw":
            text_rect.topleft = (x, y)
        if align == "ne":
            text_rect.topright = (x, y)
        if align == "sw":
            text_rect.bottomleft = (x, y)
        if align == "se":
            text_rect.bottomright = (x, y)
        if align == "n":
            text_rect.midtop = (x, y)
        if align == "s":
            text_rect.midbottom = (x, y)
        if align == "e":
            text_rect.midright = (x, y)
        if align == "w":
            text_rect.midleft = (x, y)
        if align == "center":
            text_rect.center = (x, y)
        self.screen.blit(text_surface, text_rect)

    def draw_player_weapon(self, surf, x, y, weapon):
        self.outline_rect = pg.Rect(x, y, TILESIZE + 4, TILESIZE + 4)
        self.img_rect = pg.Rect(x + 2, y + 2, TILESIZE, TILESIZE)
        pg.draw.rect(surf, C1, self.outline_rect, 2)
        surf.blit(weapon, self.img_rect)

    def draw_keys(self, surf, x, y, num):
        game_folder = path.dirname(__file__)
        asset_folder = path.join(game_folder, 'assets')
        self.key_img = pg.image.load(path.join(asset_folder, ITEM_IMAGES['key'])).convert_alpha()
        self.key_img = pg.transform.scale(self.key_img, (24, 24))
        self.img_rect = self.key_img.get_rect()
        self.bg_rect = pg.Rect(x + 2, y + 2, TILESIZE + 2, TILESIZE + 22)
        self.outline_rect = pg.Rect(x, y, TILESIZE + 4, TILESIZE + 24)
        pg.draw.rect(surf, BG_COLOR, self.bg_rect)
        pg.draw.rect(surf, C1, self.outline_rect, 2)
        surf.blit(self.key_img, (x + 6, y + 6))
        self.draw_text(f'x{num}', self.font, 10, C1, x + 19, y + 40, align="center")

    def draw_coins(self, surf, x, y, num):
        game_folder = path.dirname(__file__)
        asset_folder = path.join(game_folder, 'assets')
        self.coin_img = pg.image.load(path.join(asset_folder, ITEM_IMAGES['coin'])).convert_alpha()
        self.coin_img = pg.transform.scale(self.coin_img, (24, 24))
        self.img_rect = self.coin_img.get_rect()
        self.bg_rect = pg.Rect(x + 2, y + 2, TILESIZE + 2, TILESIZE + 22)
        self.outline_rect = pg.Rect(x, y, TILESIZE + 4, TILESIZE + 24)
        pg.draw.rect(surf, BG_COLOR, self.bg_rect)
        pg.draw.rect(surf, C1, self.outline_rect, 2)
        surf.blit(self.coin_img, (x + 6, y + 6))
        self.draw_text(f'x{num}', self.font, 10, C1, x + 19, y + 40, align="center")

    def draw_player_health(self, surf, x, y, pct):
        if pct < 0:
            pct = 0
        fill = pct * 100
        self.outline_rect = pg.Rect(x, y, 100, 20)
        self.fill_rect = pg.Rect(x, y, fill, 20)
        self.bg_rect = pg.Rect(x, y, 100, 20)
        pg.draw.rect(surf, BG_COLOR, self.bg_rect)
        pg.draw.rect(surf, C4, self.fill_rect)
        pg.draw.rect(surf, C1, self.outline_rect, 2)
        self.draw_text(f'~{self.player.health}', self.font, 10, C1, x + 10 , y + 10, align="w")

    def draw_player_armor(self, surf, x, y, pct):
        if pct < 0:
            pct = 0
        fill = pct * 67
        self.outline_rect = pg.Rect(x, y, 67, 10)
        self.fill_rect = pg.Rect(x, y, fill, 10)
        self.bg_rect = pg.Rect(x, y, 67, 10)
        pg.draw.rect(surf, BG_COLOR, self.bg_rect)
        pg.draw.rect(surf, C8, self.fill_rect)
        pg.draw.rect(surf, C1, self.outline_rect, 2)

    def load_data(self):
        game_folder = path.dirname(__file__)
        asset_folder = path.join(game_folder, 'assets')
        self.map_folder = path.join(game_folder, 'map')

        self.font = path.join(asset_folder, 'gb.ttf')
        self.dim_screen = pg.Surface(self.screen.get_size()).convert_alpha()
        self.dim_screen.fill((0, 0, 0, 180))

        self.player_img = pg.image.load(path.join(asset_folder, PLAYER_IMG)).convert_alpha()
        self.skull_img = pg.image.load(path.join(asset_folder, SKULL_IMG)).convert_alpha()
        self.chest_img = pg.image.load(path.join(asset_folder, CHEST_IMG)).convert_alpha()
        self.sign_img = pg.image.load(path.join(asset_folder, SIGN_IMG)).convert_alpha()

        self.item_images = {}
        for item in ITEM_IMAGES:
            self.item_images[item] = pg.image.load(path.join(asset_folder, ITEM_IMAGES[item])).convert_alpha()
        self.mob_images = {}
        for mob in MOB_IMAGES:
            self.mob_images[mob] = pg.image.load(path.join(asset_folder, MOB_IMAGES[mob])).convert_alpha()
        self.load_user_data()

    def load_user_data(self):
        self.data = open("user_data.txt", "r").readlines()
        for i in range(len(self.data)-1, -1, -1):
            self.data[i] = self.data[i].rstrip("\n")
            if i % 2 == 0:
                self.data.remove(self.data[i])

    def save_user_data(self, coins):
        data = open("user_data.txt", "r").readlines()
        data[1] = str(coins) + '\n'
        out = open("user_data.txt", "w")
        out.writelines(data)
        out.close()

    def new(self):
        self.all_sprites = pg.sprite.LayeredUpdates()
        self.walls = pg.sprite.Group()
        self.mobs = pg.sprite.Group()
        self.items = pg.sprite.Group()
        self.chests = pg.sprite.Group()
        self.signs = pg.sprite.Group()
        self.map = TiledMap(path.join(self.map_folder, 'f.tmx'))
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()

        for tile_object in self.map.tmxdata.objects:
            if tile_object.name == 'player':
                self.player = Player(self, tile_object.x, tile_object.y)
            if tile_object.name in ['mob1', 'mob2', 'mob3', 'mob4']:
                Mob(self, tile_object.x, tile_object.y, tile_object.name)
            if tile_object.name == 'wall':
                Obstacle(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)
            if tile_object.name in ['heart', 'weapon1', 'weapon2', 'weapon3', 'weapon4', 'weapon5', 'weapon6', 'weapon7', 'weapon8', 'key', 'coin', 'armor1', 'armor2', 'armor3']:
                Item(self, tile_object.x, tile_object.y, tile_object.name)
            if tile_object.name == 'chest':
                Chest(self, tile_object.x, tile_object.y)
            if 'sign' in tile_object.name:
                self.sign_texts = {}
                for text in SIGN_TEXTS:
                    self.sign_texts[text] = Sign(self, tile_object.x, tile_object.y, SIGN_TEXTS[tile_object.name])
        self.camera = Camera(self.map.width, self.map.height)
        self.draw_debug = False
        self.paused = False

    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            if not self.paused:
                self.update()
                self.events()
            if self.paused:
                self.pause()
            self.draw()

    def quit(self):
        self.running = False
        self.save_user_data(self.player.coins)
        pg.quit()
        sys.exit()

    def update(self):
        self.all_sprites.update()
        self.camera.update(self.player)
        if len(self.mobs) == 0:
            self.playing == False
        if self.player.health <= 0:
            self.playing = False

    def pause(self):
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                self.paused = not self.paused
                self.save_user_data(self.player.coins)

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                if event.key == pg.K_a or event.key == pg.K_LEFT:
                    self.player.move(dx = -1)
                    for mob in self.mobs:
                        mob.move_toward()
                if event.key == pg.K_d or event.key == pg.K_RIGHT:
                    self.player.move(dx = 1)
                    for mob in self.mobs:
                        mob.move_toward()
                if event.key == pg.K_w or event.key == pg.K_UP:
                    self.player.move(dy = -1)
                    for mob in self.mobs:
                        mob.move_toward()
                if event.key == pg.K_s or event.key == pg.K_DOWN:
                    self.player.move(dy = 1)
                    for mob in self.mobs:
                        mob.move_toward()
                if event.key == pg.K_h:
                    self.draw_debug = not self.draw_debug
                if event.key == pg.K_p:
                    self.paused = not self.paused

    def draw(self):
        pg.display.set_caption("{} FPS: {:.2f}".format(TITLE, self.clock.get_fps()))
        # self.screen.fill(BG_COLOR)
        self.screen.blit(self.map_img, self.camera.apply_rect(self.map_rect))
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        if self.draw_debug:
            for wall in self.walls:
                pg.draw.rect(self.screen, C2, self.camera.apply_rect(wall.rect), 1)
        self.draw_player_health(self.screen, 10, 10, self.player.health / PLAYER_HEALTH)
        self.draw_player_armor(self.screen, 43, 30, self.player.armor / PLAYER_ARMOR)
        self.draw_player_weapon(self.screen, 10, 30, self.player.weapon_img)
        self.draw_keys(self.screen, (WIDTH / 2) - TILESIZE - 10, 10, self.player.keys)
        self.draw_coins(self.screen, (WIDTH / 2), 10, self.player.coins)
        if self.paused:
            self.screen.blit(self.dim_screen, (0, 0))
            self.draw_text("paused", self.font, 30, C1, WIDTH / 2, HEIGHT / 2, align="center")
        pg.display.flip()

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        self.screen.fill(C6)
        self.draw_text("game over", self.font, 30, C1, WIDTH / 2, HEIGHT * 4 / 9, align="center")
        self.draw_text("press a key to start", self.font, 23, C1, WIDTH / 2, HEIGHT * 5 / 9, align="center")
        pg.display.flip()
        self.wait_for_key()

    def wait_for_key(self):
        pg.event.wait()
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.quit()
                if event.type == pg.KEYUP:
                    waiting = False

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.run()
    g.show_go_screen()