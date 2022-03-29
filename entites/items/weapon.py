from __future__ import annotations

from dataclasses import dataclass
from random import randint
from entites.ability import CombatAbility, Range
from entites.creature import Creature
from entites.items.equipment import Equipment, Modifier
from entites.monsters.monster import Monster
from systems.attributes import Attribute
from systems.stats import Stat


class Weapon(Equipment):
    def __init__(self) -> None:
        super().__init__()
        self.dmgType = None
        self.element = None
        self.attack = None

    def getAttack(self):
        return self.attack

    def equip(self, user: Creature) -> bool:
        equipped = super().equip(user)
        if equipped:
            self.attack.setUser(user)
        return equipped
