TITLE = 'ROGUELIKE'
WIDTH = 512
HEIGHT = 768
FPS = 60

TILESIZE = 32
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = WIDTH / TILESIZE

# DREAMSCAPE8 - https://lospec.com/palette-list/dreamscape8
C1 = (201, 204, 161)     # LIGHT GREEN
C2 = (202, 160, 90)      # YELLOW
C3 = (174, 106, 71)      # ORANGE
C4 = (139, 64, 73)       # RED
C5 = (84, 51, 68)        # DARK RED
C6 = (81, 82, 98)        # DARK BLUE
C7 = (99, 120, 125)      # BLUE
C8 = (142, 160, 145)     # LIGHT BLUE
BG_COLOR = (71, 45, 60)

PLAYER_IMG = 'player.png'
PLAYER_DAMAGE = 10
PLAYER_HEALTH = 500
PLAYER_ARMOR = 5
MOBS = {'mob1': 'mob1.png', 'mob1_health': 30, 'mob1_damage': 10,
        'mob2': 'mob2.png', 'mob2_health': 20, 'mob2_damage': 20,
        'mob3': 'mob3.png', 'mob3_health': 30, 'mob3_damage': 20,
        'mob4': 'mob4.png', 'mob4_health': 50, 'mob4_damage': 20,
        'mob5': 'mob5.png', 'mob5_health': 60, 'mob5_damage': 20,
        'mob6': 'mob6.png', 'mob6_health': 60, 'mob6_damage': 30,
        'mob7': 'mob7.png', 'mob7_health': 30, 'mob7_damage': 40,
        'mob8': 'mob8.png', 'mob8_health': 30, 'mob8_damage': 30,
        'mob9': 'mob9.png', 'mob9_health': 80, 'mob9_damage': 20}
SKULL_IMG = 'skull.png'
CHEST_IMG = 'chest.png'
INTERACT_TEXTS = {'interact1': 'Welcome :D',
                  'interact2': 'Made by Java :3',
                  'interact3': 'fin',
                  'interact4': "VALOR: Hey there! Controls are WASD or arrow keys, 'q' to use potions, 'e' to pause and open upgrades and stats. To upgrade, collect books and click '1' or '2' in upgrade menu for health upgrade or armor upgrade. "}

PLAYER_LAYER = 3
MOB_LAYER = 3
WALL_LAYER = 2
ITEMS_LAYER = 1

ITEM_IMAGES = {'heart': 'heart.png',
               'coin': 'coin.png',
               'key': 'key.png',
               'potion': 'potion.png',
               'book': 'book.png',
               'weapon1': 'weapon1.png',
               'weapon2': 'weapon2.png',
               'weapon3': 'weapon3.png',
               'weapon4': 'weapon4.png',
               'weapon5': 'weapon5.png',
               'weapon6': 'weapon6.png',
               'weapon7': 'weapon7.png',
               'weapon8': 'weapon8.png',
               'weapon9': 'weapon9.png',
               'weapon10': 'weapon10.png',
               'weapon11': 'weapon11.png',
               'weapon12': 'weapon12.png',
               'armor1': 'armor1.png',
               'armor2': 'armor2.png',
               'armor3': 'armor3.png'}
COINS = 'coins.png'
ITEM_AMOUNT = {'heart': 50,
               'potion': 50,
               'weapon1': 0,
               'weapon2': 5,
               'weapon3': 10,
               'weapon4': 5,
               'weapon5': 10,
               'weapon6': 15,
               'weapon7': 20,
               'weapon8': 20,
               'weapon9': 10,
               'weapon10': 15,
               'weapon11': 10,
               'weapon12': 15,
               'armor1': 2,
               'armor2': 4,
               'armor3': 6}
TRAVEL_LIST = ['travel1',
               'travel2',
               'travel3', 
               'travel4', 
               'travel5', 
               'travel6', 
               'travel7', 
               'travel8', 
               'travel9']

ITEMS = {'heart': 'heart.png', 'heart_amount': 50,
         'potion': 'potion.png', 'potion_amount': 50,
         'coin': 'coin.png', 
         'key': 'key.png',
         'book': 'book.png',
         'weapon1': 'weapon1.png', 'weapon1_amount': 0,
         'weapon2': 'weapon2.png', 'weapon2_amount': 5,
         'weapon3': 'weapon3.png', 'weapon3_amount': 10,
         'weapon4': 'weapon4.png', 'weapon4_amount': 5,
         'weapon5': 'weapon5.png', 'weapon5_amount': 10,
         'weapon6': 'weapon6.png', 'weapon6_amount': 15,
         'weapon7': 'weapon7.png', 'weapon7_amount': 20,
         'weapon8': 'weapon8.png', 'weapon8_amount': 20,
         'weapon9': 'weapon9.png', 'weapon9_amount': 10,
         'weapon10': 'weapon10.png', 'weapon10_amount': 15,
         'weapon11': 'weapon11.png', 'weapon11_amount': 10,
         'weapon12': 'weapon12.png', 'weapon12_amount': 15,
         'armor1': 'armor1.png', 'armor1_amount': 2,
         'armor2': 'armor2.png', 'armor2_amount': 4,
         'armor3': 'armor3.png', 'armor3_amount': 6}