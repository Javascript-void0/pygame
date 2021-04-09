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
MOB_IMAGES = {'mob1': 'mob1.png',
              'mob2': 'mob2.png',
              'mob3': 'mob3.png',
              'mob4': 'mob4.png'}
SKULL_IMG = 'skull.png'
CHEST_IMG = 'chest.png'
SIGN_IMG = 'sign.png'
SIGN_TEXTS = {'sign1': 'Welcome :D',
              'sign2': 'Made by Java :3',
              'sign3': '<<< Enter :P'}

PLAYER_DAMAGE = 10
PLAYER_HEALTH = 5000
PLAYER_ARMOR = 5
MOB1_DAMAGE = 10
MOB1_HEALTH = 30
MOB2_DAMAGE = 20
MOB2_HEALTH = 20
MOB3_DAMAGE = 20
MOB3_HEALTH = 30
MOB4_DAMAGE = 20
MOB4_HEALTH = 50

PLAYER_LAYER = 3
MOB_LAYER = 3
WALL_LAYER = 2
ITEMS_LAYER = 1

ITEM_IMAGES = {'heart': 'heart.png',
               'coin': 'coin.png',
               'key': 'key.png',
               'weapon1': 'weapon1.png',
               'weapon2': 'weapon2.png',
               'weapon3': 'weapon3.png',
               'weapon4': 'weapon4.png',
               'weapon5': 'weapon5.png',
               'weapon6': 'weapon6.png',
               'weapon7': 'weapon7.png',
               'weapon8': 'weapon8.png',
               'armor1': 'armor1.png',
               'armor2': 'armor2.png',
               'armor3': 'armor3.png'}
HEART_AMOUNT = 50
WEAPON1_AMOUNT = 0
WEAPON2_AMOUNT = 5
WEAPON3_AMOUNT = 10
WEAPON4_AMOUNT = 5
WEAPON5_AMOUNT = 10
WEAPON6_AMOUNT = 15
WEAPON7_AMOUNT = 20
WEAPON8_AMOUNT = 20
ARMOR1_AMOUNT = 2
ARMOR2_AMOUNT = 4
ARMOR3_AMOUNT = 6

TRAVEL_LIST = ['travel1',
               'travel2',
               'travel3', 
               'travel4', 
               'travel5', 
               'travel6', 
               'travel7', 
               'travel8', 
               'travel9']