import pygame as pg
import sys
import random
from os import path
from pygame import mixer
from settings import *
from sprites import *
from tilemap import *
from draw import *

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.running = True
        pg.key.set_repeat(200, 100)
        self.load_data()

    def load_data(self):
        game_folder = path.dirname(__file__)
        self.asset_folder = path.join(game_folder, 'assets')
        self.map_folder = path.join(game_folder, 'map')

        self.font = path.join(self.asset_folder, 'gb.ttf')
        self.dim_screen = pg.Surface(self.screen.get_size()).convert_alpha()
        self.dim_screen.fill((0, 0, 0, 180))

        self.player_img = pg.image.load(path.join(self.asset_folder, PLAYER_IMG)).convert_alpha()
        self.skull_img = pg.image.load(path.join(self.asset_folder, SKULL_IMG)).convert_alpha()
        self.chest_img = pg.image.load(path.join(self.asset_folder, CHEST_IMG)).convert_alpha()
        self.sign_img = pg.image.load(path.join(self.asset_folder, SIGN_IMG)).convert_alpha()

        self.item_images = {}
        for item in ITEM_IMAGES:
            self.item_images[item] = pg.image.load(path.join(self.asset_folder, ITEM_IMAGES[item])).convert_alpha()
        self.mob_images = {}
        for mob in MOB_IMAGES:
            self.mob_images[mob] = pg.image.load(path.join(self.asset_folder, MOB_IMAGES[mob])).convert_alpha()
        self.load_user_data()
        self.sound = pg.mixer.Sound(path.join(self.asset_folder, 'obstacle.wav'))
        self.sound.set_volume(0.008)
        self.footstep = pg.mixer.Sound(path.join(self.asset_folder, 'footstep.wav'))
        self.footstep.set_volume(0.03)

    def load_user_data(self):
        self.data = open("user_data.txt", "r").readlines()
        for i in range(len(self.data)-1, -1, -1):
            self.data[i] = self.data[i].rstrip("\n")
            if i % 2 == 0:
                self.data.remove(self.data[i])

    def save_user_data(self):
        data = open("user_data.txt", "r").readlines()
        data[1] = str(self.player.coins) + '\n'
        out = open("user_data.txt", "w")
        out.writelines(data)
        out.close()

    def new(self, map, health = PLAYER_HEALTH, 
            damage = PLAYER_DAMAGE, 
            armor = PLAYER_ARMOR, 
            weapon = 'weapon1', 
            keys = 0, 
            potions = 0, 
            books = 0, 
            health_upgrade = 0, 
            armor_upgrade = 0, 
            moves = 0):
        self.all_sprites = pg.sprite.LayeredUpdates()
        self.walls = pg.sprite.Group()
        self.mobs = pg.sprite.Group()
        self.items = pg.sprite.Group()
        self.chests = pg.sprite.Group()
        self.signs = pg.sprite.Group()
        self.travels = pg.sprite.Group()
        self.map_name= map
        self.map = TiledMap(path.join(self.map_folder, map))
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()

        for tile_object in self.map.tmxdata.objects:
            if tile_object.name == 'player':
                self.player = Player(self, tile_object.x, tile_object.y, health, damage, armor, weapon, keys, potions, books, health_upgrade, armor_upgrade, moves)
            if tile_object.name in MOB_LIST:
                Mob(self, tile_object.x, tile_object.y, tile_object.name)
            if tile_object.name == 'mob':
                random_mob = random.choice(MOB_LIST)
                Mob(self, tile_object.x, tile_object.y, random_mob)
            if tile_object.name == 'wall':
                Obstacle(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)
            if tile_object.name in ITEM_LIST:
                Item(self, tile_object.x, tile_object.y, tile_object.name)
            if tile_object.name == 'item':
                random_item = random.choice(ITEM_LIST)
                Item(self, tile_object.x, tile_object.y, random_item)
            if tile_object.name == 'chest':
                Chest(self, tile_object.x, tile_object.y)
            if tile_object.name == 'travel' or tile_object.name in TRAVEL_LIST:
                Travel(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height, tile_object.name)
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
        self.save_user_data()
        pg.quit()
        sys.exit()

    def update(self):
        self.all_sprites.update()
        self.camera.update(self.player)
        if self.player.health <= 0:
            self.player.health = 0
            self.playing = False

    def pause(self):
        pg.mixer.music.pause()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                elif event.key == pg.K_1:
                    cost = (self.player.health_upgrade + 1) * 2
                    if self.player.books >= cost:
                        self.player.books -= cost
                        self.player.health_upgrade += 1
                        self.player.health = PLAYER_HEALTH + (20 * self.player.health_upgrade)
                elif event.key == pg.K_2:
                    cost = (self.player.armor_upgrade + 1) * 2
                    if self.player.books >= cost:
                        self.player.books -= cost
                        self.player.armor_upgrade += 1
                        self.player.armor = PLAYER_ARMOR + self.player.armor_upgrade
                else:
                    self.paused = not self.paused
                    pg.mixer.music.unpause()
                    self.save_user_data()

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
                if event.key == pg.K_e:
                    self.paused = not self.paused
                if event.key == pg.K_q:
                    if self.player.health < PLAYER_HEALTH and self.player.potions > 0:
                        self.player.potions -= 1
                        self.player.health += POTION_AMOUNT
                        if self.player.health > PLAYER_HEALTH:
                            self.player.health = PLAYER_HEALTH

    def draw(self):
        pg.display.set_caption("{} FPS: {:.2f} ({}, {}) MAP: {}".format(TITLE, self.clock.get_fps(), self.player.x / TILESIZE, self.player.y / TILESIZE, self.map_name))
        # self.screen.fill(BG_COLOR)
        self.screen.blit(self.map_img, self.camera.apply_rect(self.map_rect))
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        if self.draw_debug:
            for wall in self.walls:
                pg.draw.rect(self.screen, C2, self.camera.apply_rect(wall.rect), 1)
        Draw.draw_player_health(self, self.screen, 10, 10, self.player.health / (PLAYER_HEALTH + (self.player.health_upgrade * 20)))
        Draw.draw_player_armor(self, self.screen, 43, 30, self.player.armor / (PLAYER_ARMOR + self.player.armor_upgrade))
        Draw.draw_player_weapon(self, self.screen, 10, 30, self.player.weapon_img)
        Draw.draw_top(self, self.screen, WIDTH / 2, 10)
        if self.paused:
            Draw.draw_paused(self, self.screen, (WIDTH / 2), (HEIGHT * 7 / 8) - 10)
            Draw.draw_upgrades(self, self.screen, 140, HEIGHT - 45)
            Draw.draw_player_stats(self, self.screen, (WIDTH / 2) - 80, HEIGHT - (TILESIZE * 3.5) - 10)
            Draw.draw_player_score(self, self.screen, WIDTH - 20, HEIGHT - 20)
        pg.display.flip()

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        self.screen.blit(self.dim_screen, (0, 0))
        Draw.draw_text(self, "game over", self.font, 30, C1, WIDTH / 2, HEIGHT * 4 / 9, align="center")
        Draw.draw_text(self, "press a key to start", self.font, 23, C1, WIDTH / 2, HEIGHT * 5 / 9, align="center")
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
    g.new('map.tmx')
    g.run()
    g.show_go_screen()