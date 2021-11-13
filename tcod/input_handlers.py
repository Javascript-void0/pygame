import tcod as libtcod

def handle_keys(key):
    if key.vk == libtcod.KEY_UP:
        return {'move': (0, -1)}
    elif key.vk == libtcod.KEY_DOWN:
        return {'move': (0, 1)}
    elif key.vk == libtcod.KEY_LEFT:
        return {'move': (-1, 0)}
    elif key.vk == libtcod.KEY_RIGHT:
        return {'move': (1, 0)}
    elif key.vk == libtcod.KEY_CHAR:
        if key.c == ord('w'):
            return {'move': (0, -1)}
        elif key.c == ord('s'):
            return {'move': (0, 1)}
        elif key.c == ord('a'):
            return {'move': (-1, 0)}
        elif key.c == ord('d'):
            return {'move': (1, 0)}

    if key.vk == libtcod.KEY_ENTER and key.lalt:
        return {'fullscreen': True}
    
    elif key.vk == libtcod.KEY_ESCAPE:
        return {'exit': True}
    
    return {}