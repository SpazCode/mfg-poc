from enum import Enum
from random import randint
from entites.creature import Creature
from systems.stats import Stat


def doesHit(acc: float, target: Creature) -> bool:
    accMod = abs(target.stats[Stat.EVD] - acc)
    hitScore = acc if acc > target.stats[Stat.EVD] else max(
                    15, acc - accMod)
    return randint(0, 100) <= hitScore


class DamageType(Enum):
    SLASH = 1
    PIERCE = 2
    FIRE = 3
    WATER = 4
    WIND = 5
    LIGHTNING = 6
    EARTH = 7
    ICE = 8
