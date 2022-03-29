from __future__ import annotations

from enum import IntEnum
from typing import Any, overload

from systems.attributes import Attribute, Attributes


class Creature(object):

    def __init__(self) -> None:
        self.currentHP = 0
        self.HP = 5
        self.currentMP = 0
        self.MP = 5
        self._attributes = Attributes()

    def resetHP(self) -> Creature:
        self.currentHP = self.HP
        return self

    def getCurrentHP(self) -> int:
        return self.currentHP

    def setCurrentHP(self, value: int) -> Creature:
        self.currentHP = value
        return self

    def getHP(self) -> int:
        return self.HP

    def setHP(self, value: int) -> Creature:
        self.HP = value
        return self

    def resetMP(self) -> Creature:
        self.currentMP = self.MP
        return self

    def getCurrentMP(self) -> int:
        return self.currentMP

    def setCurrentMP(self, value: int) -> Creature:
        self.currentMP = value
        return self

    def getMP(self) -> int:
        return self.MP

    def setMP(self, value: int) -> Creature:
        self.MP = value
        return self

    def getSTR(self) -> int:
        return self._attributes[Attribute.STR]

    def setSTR(self,  value: int) -> Creature:
        self._attributes[Attribute.STR] = value
        return self

    def getDEX(self) -> int:
        return self._attributes[Attribute.DEX]

    def setDEX(self, value: int) -> Creature:
        self._attributes[Attribute.DEX] = value
        return self

    def getCON(self) -> int:
        return self._attributes[Attribute.CON]

    def setCON(self,  value: int) -> Creature:
        self._attributes[Attribute.CON] = value
        return self

    def getINT(self) -> int:
        return self._attributes[Attribute.INT]

    def setINT(self, value: int) -> Creature:
        self._attributes[Attribute.INT] = value
        return self

    def getWIS(self) -> int:
        return self._attributes[Attribute.WIS]

    def setWIS(self, value: int) -> Creature:
        self._attributes[Attribute.WIS] = value
        return self

    def getCHA(self) -> int:
        return self._attributes[Attribute.CHA]

    def setCHA(self, value: int) -> Creature:
        self._attributes[Attribute.CHA] = value
        return self

    def getAttributes(self) -> Attributes:
        return self._attributes

    @overload
    def updateStats(self) -> Creature:
        return self


class CreatureSize(IntEnum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    HUGE = 4
    MONSTEROUS = 5
    BOSS = 10
