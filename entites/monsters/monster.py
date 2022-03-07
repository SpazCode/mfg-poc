from __future__ import annotations

from entites.ability import Ability, AbilitySet, TargetType
from entites.creature import Creature, CreatureSize


class Monster(Creature):

    def __init__(self) -> None:
        super().__init__()
        self.name = ''
        self.ATK = 0
        self.DEF = 0
        self.MAG = 0
        self.RES = 0
        self.SPD = 0
        self.size = CreatureSize.MEDIUM
        self.abilities = AbilitySet()

    def getName(self) -> str:
        return self.name

    def setName(self, value: str) -> Monster:
        self.name = value
        return self

    def updateStats(self) -> Creature:
        self.ATK = max(1,  6 + (int(self.STR / 2) - 5) +
                       (int(self.DEX / 4) - 3))
        self.DEF = max(1,  6 + (int(self.CON / 2) - 5) +
                       (int(self.DEX / 4) - 3))
        self.MAG = max(1,  6 + (int(self.INT / 2) - 5) +
                       (int(self.WIS / 4) - 3))
        self.RES = max(1,  6 + (int(self.WIS / 2) - 5) +
                       (int(self.CHA / 4) - 3))
        self.SPD = max(1, 8 + (int(self.DEX / 2) - 3)
                       + (int(self.CHA / 4) - 3))
        return self

    def getStatBlock(self) -> str:
        return 'Name: {0} - HP: {6}, ATK: {1}, DEF: {2}, MAG: {3}, RES: {4}, SPD: {5}'.format(self.name, self.ATK, self.DEF, self.MAG, self.RES, self.SPD, self.HP)

    def __str__(self) -> str:
        return self.name