from __future__ import annotations
from ast import Attribute

from dataclasses import dataclass
from random import randint
from entites.ability import Ability, CombatAbility, Range
from entites.creature import Creature
from entites.items.equipment import Equipment, Modifier
from entites.monsters.monster import Monster
from systems.stats import Stat


class Weapon(Equipment):
    def __init__(self) -> None:
        super().__init__()
        self.dmgType = None
        self.element = None
        self.skills = list
        self.attack = None


@dataclass
class WeaponSkill(object):
    requirements: list
    skill: Ability


class BareHanded(Weapon):
    def __init__(self) -> None:
        super().__init__()
        self.stats[Stat.ATK] = 5
        self.stats[Stat.ACC] = 80
        self.modifiers[Stat.ATK] = Modifier(
            attribute=Attribute.STR, multiplyer=1.0, useMod=True)
        self.attack = BareHanded.Attack(self.equipedUser, self.stats[Stat.ACC])

    class Attack(CombatAbility):
        def __init__(self, user: Creature, accuracy: int) -> None:
            super().__init__(user)
            self.name = 'Unarmed Strke'
            self.description = 'Unarmed strike made with your open hand'
            self.range = Range.CLOSE
            self.accuracy = accuracy

        def execute(self, target: Monster) -> None:
            if target is not None:
                dmg = max(1, target.DEF - self.user.stats[Stat.ATK])
                accMod = abs(target.stats[Stat.EVD] - self.accuracy)
                hitScore = self.accuracy if self.accuracy > target.stats[Stat.EVD] else max(15, self.accuracy - accMod)
                hit = randint(0, 100) <= hitScore
                if hit: 
                    print('{0} hit {1} dealing {2} Damage'.format(
                        self.user.getName(), target.getName(), dmg))
                    target.setCurrentHP(max(0, target.getCurrentHP() - dmg))
                    return
                else:
                    print('{0} missed {1}'.format(
                        self.user.getName(), target.getName()))
                    return
            print("No Target Specifed")
