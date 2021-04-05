import pygame as pg
import sys
import random
from os import path
from settings import *
from sprites import *
from tilemap import *

def draw_player_health(surf, x, y, pct):
    if pct < 0:
        pct = 0
    BAR_LENGTH = 100
    BAR_HEIGHT = 20
    fill = pct * BAR_LENGTH
    outline_rect = pg.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pg.Rect(x, y, fill, BAR_HEIGHT)
    bg_rect = pg.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    col = C4
    bg = BG_COLOR
    pg.draw.rect(surf, bg, bg_rect)
    pg.draw.rect(surf, col, fill_rect)
    pg.draw.rect(surf, C1, outline_rect, 2)

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.running = True
        pg.key.set_repeat(500, 100)
        self.load_data()

    def load_data(self):
        game_folder = path.dirname(__file__)
        asset_folder = path.join(game_folder, 'assets')
        map_folder = path.join(game_folder, 'map')
        self.map = TiledMap(path.join(map_folder, 'f.tmx'))
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()

        self.player_img = pg.image.load(path.join(asset_folder, PLAYER_IMG)).convert_alpha()
        self.player_img = pg.transform.scale(self.player_img, (TILESIZE, TILESIZE))
        self.mob_img = pg.image.load(path.join(asset_folder, MOB_IMG)).convert_alpha()
        self.mob_img = pg.transform.scale(self.mob_img, (TILESIZE, TILESIZE))
        self.wall_img = pg.image.load(path.join(asset_folder, WALL_IMG)).convert_alpha()
        self.wall_img = pg.transform.scale(self.wall_img, (TILESIZE, TILESIZE))

        self.item_images = {}
        for item in ITEM_IMAGES:
            self.item_images[item] = pg.image.load(path.join(asset_folder, ITEM_IMAGES[item])).convert_alpha()

    def new(self):
        self.all_sprites = pg.sprite.LayeredUpdates()
        self.walls = pg.sprite.Group()
        self.mobs = pg.sprite.Group()
        self.items = pg.sprite.Group()

        for tile_object in self.map.tmxdata.objects:
            if tile_object.name == 'player':
                self.player = Player(self, tile_object.x, tile_object.y)
            if tile_object.name == 'mob':
                Mob(self, tile_object.x, tile_object.y)
            if tile_object.name == 'wall':
                Obstacle(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)
            if tile_object.name in ['heart']:
                Item(self, tile_object.x, tile_object.y, tile_object.name)
        self.camera = Camera(self.map.width, self.map.height)
        self.draw_debug = False

    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        self.running = False
        pg.quit()
        sys.exit()

    def update(self):
        self.all_sprites.update()
        self.camera.update(self.player)

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                if event.key == pg.K_a:
                    self.player.move(dx = -1)
                    for mob in self.mobs:
                        mob.move_toward()
                if event.key == pg.K_d:
                    self.player.move(dx = 1)
                    for mob in self.mobs:
                        mob.move_toward()
                if event.key == pg.K_w:
                    self.player.move(dy = -1)
                    for mob in self.mobs:
                        mob.move_toward()
                if event.key == pg.K_s:
                    self.player.move(dy = 1)
                    for mob in self.mobs:
                        mob.move_toward()
                if event.key == pg.K_h:
                    self.draw_debug = not self.draw_debug

    def draw(self):
        pg.display.set_caption("{} FPS: {:.2f}".format(TITLE, self.clock.get_fps()))
        # self.screen.fill(BG_COLOR)
        self.screen.blit(self.map_img, self.camera.apply_rect(self.map_rect))
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        if self.draw_debug:
            for wall in self.walls:
                pg.draw.rect(self.screen, C2, self.camera.apply_rect(wall.rect), 1)
        draw_player_health(self.screen, 10, 10, self.player.health / PLAYER_HEALTH)
        pg.display.flip()

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.run()
    g.show_go_screen()