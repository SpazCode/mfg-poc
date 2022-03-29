from __future__ import annotations

from random import randint
from entites.ability import Ability, AbilitySet, TargetType
from entites.creature import Creature, CreatureSize
from systems.stats import Stat, Stats
from systems.party import Party


class Monster(Creature):

    def __init__(self) -> None:
        super().__init__()
        self.name = ''
        self.stats = Stats()
        self.size = CreatureSize.MEDIUM
        self.abilities = AbilitySet()

    def getName(self) -> str:
        return self.name

    def setName(self, value: str) -> Monster:
        self.name = value
        return self

    def setATK(self, value: int) -> Monster:
        self.stats[Stat.ATK] = value
        return self

    def setDEF(self, value: int) -> Monster:
        self.stats[Stat.DEF] = value
        return self

    def setMAG(self, value: int) -> Monster:
        self.stats[Stat.MAG] = value
        return self

    def setRES(self, value: int) -> Monster:
        self.stats[Stat.RES] = value
        return self

    def setACC(self, value: int) -> Monster:
        self.stats[Stat.ACC] = value
        return self

    def setEVD(self, value: int) -> Monster:
        self.stats[Stat.EVD] = value
        return self

    def setSPD(self, value: int) -> Monster:
        self.stats[Stat.SPD] = value
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

            # If there are no more abilities to try we do noting
            if ability is None or ability in tried:
                print("%s does nothing".format(self.name))
                return

            tried.append(ability)

            if not ability.canUse():
                continue

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
