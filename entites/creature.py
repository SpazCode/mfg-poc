from __future__ import annotations

from enum import IntEnum
from typing import Any, overload


class Creature(object):

    def __init__(self) -> None:
        self.currentHP = 0
        self.HP = 5
        self.STR = 1
        self.DEX = 1
        self.CON = 1
        self.INT = 1
        self.WIS = 1
        self.CHA = 1

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

    def getSTR(self) -> int:
        return self.STR

    def setSTR(self,  value: int) -> Creature:
        self.STR = value
        return self

    def getDEX(self) -> int:
        return self.DEX

    def setDEX(self, value: int) -> Creature:
        self.DEX = value
        return self

    def getCON(self) -> int:
        return self.CON

    def setCON(self,  value: int) -> Creature:
        self.CON = value
        return self

    def getINT(self) -> int:
        return self.INT

    def setINT(self, value: int) -> Creature:
        self.INT = value
        return self

    def getWIS(self) -> int:
        return self.WIS

    def setWIS(self, value: int) -> Creature:
        self.WIS = value
        return self

    def getCHA(self) -> int:
        return self.CHA

    def setCHA(self, value: int) -> Creature:
        self.CHA = value
        return self

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
