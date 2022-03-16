from __future__ import annotations
from dataclasses import dataclass
from enum import Enum

from typing import overload
from entites.ability import Ability
from entites.creature import Creature
from entites.items.item import Item
from systems.attributes import Attribute, Attributes


class Equipment(Item):

    def __init__(self) -> None:
        super().__init__()
        self.equipedUser = None
        self.stats = dict()
        self.modifiers = dict()
        self.requirements = dict()
        self.skills = list()

    def canEquip(self, attributes: Attribute) -> bool:
        for req in self.requirements:
            if attributes[req] < self.requirements[req]:
                return False
        return True

    def equip(self, user: Creature) -> bool:
        if not self.canEquip(user.getAttributes()):
            return False
        self.equipedUser = user
        return True

    def modifyStats(self, attributes: Attributes) -> dict:
        mod = {}
        for stat in self.stats.keys():
            mod[stat] = self.stats[stat]
            if stat in self.modifiers.keys():
                mod[stat] += self.modifiers[stat].multiplyer * attributes.getModifier(
                    self.modifiers[stat].attribute) if self.modifiers[stat].useMod else attributes[self.modifiers[stat].attribute]
        return mod

    def addEquipmentSkill(self, type: str, reqs: list, ability: Ability) -> Equipment:
        self.skills.append(EquipmentSkill(type, reqs, ability))


@dataclass
class Modifier(object):
    attribute: Attribute
    multiplyer: float
    useMod: bool


@dataclass
class EquipmentSkill(object):
    skillType: str
    requirements: list
    skill: Ability

    def canUse(self, attributes: Attribute) -> bool:
        for req in self.requirements:
            if attributes[req] < self.requirements[req]:
                return False
        return True


class EquipentSlots(Enum):
    MAIN_HAND = 1
    OFF_HAND = 2
    HEAD = 3
    BODY = 4
    ARMS = 5
    LEGS = 6
    ACCESSORY_1 = 7
    ACCESSORY_2 = 8


class EquipmentSet(dict):
    def __init__(self, *args, **kwargs):
        self.__setitem__(EquipentSlots.MAIN_HAND, None)
        self.__setitem__(EquipentSlots.OFF_HAND, None)
        self.__setitem__(EquipentSlots.HEAD, None)
        self.__setitem__(EquipentSlots.BODY, None)
        self.__setitem__(EquipentSlots.ARMS, None)
        self.__setitem__(EquipentSlots.LEGS, None)
        self.__setitem__(EquipentSlots.ACCESSORY_1, None)
        self.__setitem__(EquipentSlots.ACCESSORY_2, None)
        self.update(*args, **kwargs)

    def equip(self, slot: EquipentSlots, piece: Equipment):
        self.__setitem__(slot, piece)
        return self

    def __getitem__(self, key: Attribute):
        val = dict.__getitem__(self, key)
        return val

    def __setitem__(self, key: EquipentSlots, val: Equipment):
        if type(key) is not EquipentSlots:
            raise Exception('Only an EquipmentSlot can be included as the key')
        dict.__setitem__(self, key, val)

    def __repr__(self):
        dictrepr = dict.__repr__(self)
        return '%s(%s)' % (type(self).__name__, dictrepr)

    def update(self, *args, **kwargs):
        for k, v in dict(*args, **kwargs).items():
            self[k] = v
