from __future__ import annotations
from random import randint

from entites.ability import CombatAbility, Range
from entites.characters.character import Character
from entites.creature import Creature
from entites.monsters.monster import Monster
from systems.party import Party
from systems.stats import Stat


class Goblin(Monster):

    def __init__(self) -> None:
        super().__init__()
        # Initialize with default Goblin stats
        self.setSTR(12).setDEX(14).setCON(14).setINT(4).setWIS(
            5).setCHA(2).setHP(15).updateStats().resetHP()
        # Initialize the moveset
        self.abilities.setAttack(ClawAttack(
            self)).addUniqueSkill(RockThrow(self))

    def combatTurn(self, playerParty: Party, yourParty: Party):
        return super().combatTurn(playerParty, yourParty)


class ClawAttack(CombatAbility):

    def __init__(self, user: Monster) -> None:
        super().__init__(user)
        self.name = 'Claw Attack'
        self.description = ''
        self.range = Range.CLOSE

    def execute(self, target: Creature) -> None:
        if target is not None and type(target) is Character:
            dmg = max(randint(1, 4), target.stats[Stat.DEF] - self.user.stats[Stat.ATK])
            hit = int(randint(0, 10)) + (int(self.user.getDEX() / 2) - 5)
            if hit > 5:
                print('{0} hit {1} dealing {2} Damage'.format(
                    self.user.getName(), target.getName(), dmg))
                target.setCurrentHP(max(0, target.getCurrentHP() - dmg))
            else:
                print('{0} missed {1}'.format(
                    self.user.getName(), target.getName()))
        print("No Target Specifed")


class RockThrow(CombatAbility):

    def __init__(self, user: Monster) -> None:
        super().__init__(user)
        self.name = 'Rock Throw'
        self.description = ''
        self.range = Range.REACH

    def execute(self, target: Creature) -> None:
        if target is not None and type(target) is Character:
            dmg = max(1, target.stats[Stat.DEF] - self.user.stats[Stat.ATK])
            hit = int(randint(0, 10)) + (int(self.user.getDEX() / 2) - 5)
            if hit > 5:
                print('{0} hit {1} dealing {2} Damage'.format(
                    self.user.getName(), target.getName(), dmg))
                target.setCurrentHP(max(0, target.getCurrentHP() - dmg))
            else:
                print('{0} missed {1}'.format(
                    self.user.getName(), target.getName()))
        print("No Target Specifed")
