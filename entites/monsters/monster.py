from __future__ import annotations

from random import randint
from entites.ability import Ability, AbilitySet, TargetType
from entites.creature import Creature, CreatureSize
from systems import stats
from systems.party import Party


class Monster(Creature):

    def __init__(self) -> None:
        super().__init__()
        self.name = ''
        self.stats = stats()
        self.size = CreatureSize.MEDIUM
        self.abilities = AbilitySet()

    def getName(self) -> str:
        return self.name

    def setName(self, value: str) -> Monster:
        self.name = value
        return self

    def updateStats(self) -> Creature:
        self.ATK = max(1,  6 + (int(self.getSTR() / 2) - 5) +
                       (int(self.getDEX() / 4) - 3))
        self.DEF = max(1,  6 + (int(self.getCON() / 2) - 5) +
                       (int(self.getDEX() / 4) - 3))
        self.MAG = max(1,  6 + (int(self.getINT() / 2) - 5) +
                       (int(self.getWIS() / 4) - 3))
        self.RES = max(1,  6 + (int(self.getWIS() / 2) - 5) +
                       (int(self.getCHA() / 4) - 3))
        self.SPD = max(1, 8 + (int(self.getDEX() / 2) - 3)
                       + (int(self.getCHA() / 4) - 3))
        return self

    def getStatBlock(self) -> str:
        return 'Name: {0} - HP: {6}, ATK: {1}, DEF: {2}, MAG: {3}, RES: {4}, SPD: {5}'.format(self.name, self.ATK, self.DEF, self.MAG, self.RES, self.SPD, self.HP)

    def __str__(self) -> str:
        return self.name

    def combatTurn(self, playerParty: Party, yourParty: Party):
        ability = None
        target = None
        tried = []
        while target is None:
            # Pick a move at random
            abilityChoices = list(filter(
                lambda a: a not in tried, self.abilities.unique)) + [self.abilities.attack]
            choice = randint(0, len(abilityChoices) - 1)
            ability = abilityChoices[choice]

            #
            if ability is None or ability in tried:
                return

            tried.append(ability)

            if ability.targetType is TargetType.ENEMY:
                targetsInRange = list(filter(lambda m: Ability.isTargetInRange(
                    self, yourParty, m, playerParty, ability.range), playerParty.members))
                if len(targetsInRange) < 1:
                    continue
                targetIndex = randint(0, len(targetsInRange) - 1)
                target = targetsInRange[targetIndex]
            elif ability.targetType is TargetType.ALLY:
                targetsInRange = list(filter(lambda m: Ability.isTargetInRange(
                    self, yourParty, m, yourParty, ability.range), yourParty.members))
                if len(targetsInRange) < 1:
                    continue
                targetIndex = randint(0, len(targetsInRange) - 1)
                target = targetsInRange[targetIndex]

        ability.execute(target)
