TITLE = 'RPG'
WIDTH = 512
HEIGHT = 512
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
              'mob3': 'mob3.png'}
SKULL_IMG = 'skull.png'
CHEST_IMG = 'chest.png'

PLAYER_DAMAGE = 10
PLAYER_HEALTH = 500
MOB1_DAMAGE = 10
MOB1_HEALTH = 30
MOB2_DAMAGE = 20
MOB2_HEALTH = 20
MOB3_DAMAGE = 20
MOB3_HEALTH = 30

PLAYER_LAYER = 3
MOB_LAYER = 3
WALL_LAYER = 2
ITEMS_LAYER = 1

ITEM_IMAGES = {'heart': 'heart.png',
               'weapon1': 'weapon1.png',
               'weapon2': 'weapon2.png'}
HEART_AMOUNT = 50
WEAPON1_AMOUNT = 0
WEAPON2_AMOUNT = 5