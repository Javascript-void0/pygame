from components.ai import HostileEnemy
from components.fighter import Fighter
from entity import Actor

player = Actor(
    char="@", 
    color=(251, 245, 239), 
    name="Player", 
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=30, defense=2, power=5)
)

orc = Actor(
    char="o", 
    color=(60, 60, 106), 
    name="Orc", 
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3)
)

troll = Actor(
    char="T", 
    color=(60, 60, 106), 
    name="Troll", 
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=16, defense=1, power=4)
)