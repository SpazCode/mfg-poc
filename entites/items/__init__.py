
from random import randint
from entites.ability import CombatAbility, Range
from entites.creature import Creature
from entites.items.equipment import Equipment, Modifier
from entites.items.weapon import Weapon
from entites.monsters.monster import Monster
from entites.skills import CloseMeleeAttack, RangeMagicAttack, RangeMaleeAttack
from systems.attributes import Attribute
from systems.combat import doesHit
from systems.stats import Stat

# Set of Equipment that can be used by Characters.

# Bare Handed is the Equipment used when


class BareHanded(Weapon):
    def __init__(self) -> None:
        super().__init__()
        self.stats[Stat.ATK] = 5
        self.stats[Stat.MAG] = 0
        self.stats[Stat.ACC] = 80
        self.modifiers[Stat.ATK] = [
            Modifier(attribute=Attribute.STR, multiplyer=1.0, useMod=True)
        ]
        self.modifiers[Stat.MAG] = [
            Modifier(attribute=Attribute.INT, multiplyer=1.0, useMod=True)
        ]
        self.attack = CloseMeleeAttack(self.equipedUser, self.stats[Stat.ACC])


class Sword(Weapon):
    def __init__(self) -> None:
        super().__init__()
        self.stats[Stat.ATK] = 7
        self.stats[Stat.MAG] = 0
        self.stats[Stat.ACC] = 95
        self.modifiers[Stat.ATK] = [
            Modifier(attribute=Attribute.STR, multiplyer=1.0, useMod=True),
            Modifier(attribute=Attribute.DEX, multiplyer=1.0, useMod=True)
        ]
        self.attack = CloseMeleeAttack(self.equipedUser, self.stats[Stat.ACC])


class Spear(Weapon):
    def __init__(self) -> None:
        super().__init__()
        self.stats[Stat.ATK] = 7
        self.stats[Stat.MAG] = 0
        self.stats[Stat.ACC] = 95
        self.modifiers[Stat.ATK] = [
            Modifier(attribute=Attribute.DEX, multiplyer=1.00, useMod=True)
        ]
        self.attack = RangeMaleeAttack(self.equipedUser, self.stats[Stat.ACC])

class ShortBow(Weapon):
    def __init__(self) -> None:
        super().__init__()
        self.stats[Stat.ATK] = 7
        self.stats[Stat.MAG] = 0
        self.stats[Stat.ACC] = 85
        self.modifiers[Stat.ATK] = [
            Modifier(attribute=Attribute.DEX, multiplyer=1.0, useMod=True)
        ]
        self.attack = RangeMaleeAttack(self.equipedUser, self.stats[Stat.ACC])\



class Staff(Weapon):
    def __init__(self) -> None:
        super().__init__()
        self.stats[Stat.ATK] = 2
        self.stats[Stat.MAG] = 5
        self.stats[Stat.ACC] = 85
        self.modifiers[Stat.ATK] = [
            Modifier(attribute=Attribute.INT, multiplyer=1.0, useMod=True)
        ]
        self.attack = RangeMagicAttack(self.equipedUser, self.stats[Stat.ACC])


class UnArmoured(Equipment):
    def __init__(self) -> None:
        super().__init__()
        self.stats[Stat.RES] = 5
        self.stats[Stat.DEF] = 5
        self.stats[Stat.EVD] = 15
        self.modifiers[Stat.DEF] = [
            Modifier(attribute=Attribute.DEX, multiplyer=1.0, useMod=True),
            Modifier(attribute=Attribute.CON, multiplyer=1.0, useMod=True)
        ]
        self.modifiers[Stat.RES] = [
            Modifier(attribute=Attribute.WIS, multiplyer=1.0, useMod=True),
            Modifier(attribute=Attribute.CON, multiplyer=1.0, useMod=True)
        ]
