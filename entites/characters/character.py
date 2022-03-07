from __future__ import annotations

from random import randint
from entites.ability import AbilitySet, CombatAbility
from entites.creature import Creature, CreatureSize


class Character(Creature):

    def __init__(self) -> None:
        super().__init__()
        self.name = ""
        self.ATK = 1
        self.DEF = 1
        self.MAG = 1
        self.RES = 1
        self.SPD = 1
        self.size = CreatureSize.MEDIUM
        self.abilities = AbilitySet().setAttack(Character.BasicAttack(self))

    def getName(self) -> str:
        return self.name

    def setName(self, value: str) -> Character:
        self.name = value
        return self

    def getAbilitySet(self) -> AbilitySet:
        return self.abilities

    def updateStats(self) -> Character:
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

    class BasicAttack(CombatAbility):

        def __init__(self, user: Character) -> None:
            super().__init__(user)
            self.name = 'Attack'
            self.description = 'Basic attack with your main weapon'

        def execute(self, target: Creature) -> None:
            if target is not None:
                dmg = max(1, target.DEF - self.user.ATK)
                hit = int(randint(0, 10)) + (int(self.user.DEX / 2) - 5)
                if hit > 1:
                    print('{0} hit {1} dealing {2} Damage'.format(
                        self.user.getName(), target.getName(), dmg))
                    target.setCurrentHP(max(0, target.getCurrentHP() - dmg))
                    return
                else:
                    print('{0} missed {1}'.format(
                        self.user.getName(), target.getName()))
                    return
            print("No Target Specifed")
