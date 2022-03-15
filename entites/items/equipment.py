from __future__ import annotations
from dataclasses import dataclass
from enum import Enum

from typing import overload
from entites.creature import Creature
from entites.items.item import Item
from systems.attributes import Attribute, Attributes


class Equipment(Item):

    def __init__(self) -> None:
        super().__init__(self)
        self.equipedUser = None
        self.stats = dict()
        self.modifiers = dict()
        self.requirements = dict()
    
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
            for modifier in self.modifiers[stat]:
                mod[stat] += modifier.multiplyer * attributes.getModifier(
                    modifier.attribute) if modifier.useMod else attributes[modifier.attribute]
        return mod


@dataclass
class Modifier(object):
    attribute: Attribute
    multiplyer: float
    useMod: bool


class EquipentSlots(Enum):
    LEFT_HAND = 1
    RIGHT_HAND = 2
    HEAD = 3
    BODY = 4
    ARMS = 5
    LEGS = 6
    ACCESSORY_1 = 7
    ACCESSORY_2 = 8


class EquipmentSet(dict):
    def __init__(self, *args, **kwargs):
        self.__setitem__(EquipentSlots.LEFT_HAND, None)
        self.__setitem__(EquipentSlots.RIGHT_HAND, None)
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

    def __setitem__(self, key: Attribute, val: int):
        if type(key) is not Attribute:
            raise Exception('Only an Atrribute can be included')
        dict.__setitem__(self, key, val)

    def __repr__(self):
        dictrepr = dict.__repr__(self)
        return '%s(%s)' % (type(self).__name__, dictrepr)
        
    def update(self, *args, **kwargs):
        for k, v in dict(*args, **kwargs).iteritems():
            self[k] = v
