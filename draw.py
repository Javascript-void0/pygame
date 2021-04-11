import pygame as pg
from os import path
from settings import *

class Draw:
    def __init__(self):
        pg.init()
        self.game = game

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
        self.key_img = pg.image.load(path.join(self.asset_folder, ITEM_IMAGES['key'])).convert_alpha()
        self.key_img = pg.transform.scale(self.key_img, (24, 24))
        self.img_rect = self.key_img.get_rect()
        self.img_rect.topright = (x, y)
        self.bg_rect = pg.Rect(x + 2, y + 2, TILESIZE + 2, TILESIZE + 22)
        self.bg_rect.topright = (x, y)
        self.outline_rect = pg.Rect(x, y, TILESIZE + 4, TILESIZE + 24)
        self.outline_rect.topright = (x, y)
        pg.draw.rect(surf, BG_COLOR, self.bg_rect)
        pg.draw.rect(surf, C1, self.outline_rect, 2)
        surf.blit(self.key_img, (x - 30, y + 6))
        Draw.draw_text(self, f'x{num}', self.font, 10, C1, x - 17, y + 40, align="center")

    def draw_coins(self, surf, x, y, num):
        self.coin_img = pg.image.load(path.join(self.asset_folder, ITEM_IMAGES['coin'])).convert_alpha()
        self.coin_img = pg.transform.scale(self.coin_img, (24, 24))
        self.img_rect = self.coin_img.get_rect()
        self.img_rect.topleft = (x, y)
        self.bg_rect = pg.Rect(x + 2, y + 2, TILESIZE + 2, TILESIZE + 22)
        self.bg_rect.topleft = (x, y)
        self.outline_rect = pg.Rect(x, y, TILESIZE + 4, TILESIZE + 24)
        self.outline_rect.topleft = (x, y)
        pg.draw.rect(surf, BG_COLOR, self.bg_rect)
        pg.draw.rect(surf, C1, self.outline_rect, 2)
        surf.blit(self.coin_img, (x + 6, y + 6))
        Draw.draw_text(self, f'x{num}', self.font, 10, C1, x + 19, y + 40, align="center")

    def draw_potions(self, surf, x, y, num):
        self.potion_img = pg.image.load(path.join(self.asset_folder, ITEM_IMAGES['potion'])).convert_alpha()
        self.potion_img = pg.transform.scale(self.potion_img, (24, 24))
        self.img_rect = self.potion_img.get_rect()
        self.img_rect.midtop = (x, y)
        self.bg_rect = pg.Rect(x + 2, y + 2, TILESIZE + 2, TILESIZE + 22)
        self.bg_rect.midtop = (x, y)
        self.outline_rect = pg.Rect(x, y, TILESIZE + 4, TILESIZE + 24)
        self.outline_rect.midtop = (x, y)
        pg.draw.rect(surf, BG_COLOR, self.bg_rect)
        pg.draw.rect(surf, C1, self.outline_rect, 2)
        surf.blit(self.potion_img, (x - 11, y + 6))
        Draw.draw_text(self, f'x{num}', self.font, 10, C1, x + 3, y + 40, align="center")

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
        Draw.draw_text(self, f'~{self.player.health}', self.font, 10, C1, x + 10 , y + 10, align="w")

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

    def draw_upgrades(self, surf, x, y):
        self.heart_img = pg.image.load(path.join(self.asset_folder, ITEM_IMAGES['heart'])).convert_alpha()
        self.heart_img = pg.transform.scale(self.heart_img, (24, 24))
        self.img_rect = self.heart_img.get_rect()
        self.img_rect.center = (x, y)
        self.bg1 = pg.Rect(x, y, TILESIZE + 4, TILESIZE + 22)
        self.bg1.center = (x - 84, y)
        self.b1outline = pg.Rect(x, y, TILESIZE + 4, TILESIZE + 22)
        self.b1outline.center = (x - 84, y)
        pg.draw.rect(self.screen, BG_COLOR, self.bg1)
        pg.draw.rect(self.screen, C1, self.b1outline, 2)
        surf.blit(self.heart_img, (x - 95, y - 18))
        Draw.draw_text(self, f'l.{self.player.health_upgrade}', self.font, 10, C1, x - 83, y + 14, align="center")

        self.damage_img = pg.image.load(path.join(self.asset_folder, 'damage.png')).convert_alpha()
        self.damage_img = pg.transform.scale(self.damage_img, (24, 24))
        self.img_rect = self.damage_img.get_rect()
        self.img_rect.center = (x, y)
        self.bg2 = pg.Rect(x, y, TILESIZE + 4, TILESIZE + 22)
        self.bg2.center = (x - 42, y)
        self.b2outline = pg.Rect(x, y, TILESIZE + 4, TILESIZE + 22)
        self.b2outline.center = (x - 42, y)
        pg.draw.rect(self.screen, BG_COLOR, self.bg2)
        pg.draw.rect(self.screen, C1, self.b2outline, 2)
        surf.blit(self.damage_img, (x - 53, y - 18))
        Draw.draw_text(self, f'l.{self.player.damage_upgrade}', self.font, 10, C1, x - 40, y + 14, align="center")

        self.armor_img = pg.image.load(path.join(self.asset_folder, 'armor.png')).convert_alpha()
        self.armor_img = pg.transform.scale(self.armor_img, (24, 24))
        self.img_rect = self.armor_img.get_rect()
        self.img_rect.center = (x, y)
        self.bg3 = pg.Rect(x, y, TILESIZE + 4, TILESIZE + 22)
        self.bg3.center = (x, y)
        self.b3outline = pg.Rect(x, y, TILESIZE + 4, TILESIZE + 22)
        self.b3outline.center = (x, y)        
        pg.draw.rect(self.screen, BG_COLOR, self.bg3)
        pg.draw.rect(self.screen, C1, self.b3outline, 2)
        surf.blit(self.armor_img, (x - 11, y - 18))
        Draw.draw_text(self, f'l.{self.player.armor_upgrade}', self.font, 10, C1, x + 3, y + 14, align="center")

    def draw_paused(self, surf, x, y):
        self.screen.blit(self.dim_screen, (0, 0))
        Draw.draw_text(self, "paused", self.font, 30, C1, WIDTH / 2, HEIGHT / 2, align="center")
    