from __future__ import annotations

from random import randint
from entites.ability import CombatAbility, Range
from entites.characters.character import Character
from entites.creature import Creature
from entites.monsters.monster import Monster
from systems.combat import doesHit
from systems.party import Party
from systems.stats import Stat


class Goblin(Monster):

    def __init__(self) -> None:
        super().__init__()
        # Initialize with default Goblin stats
        self.setATK(3).setDEF(3).setRES(1).setMAG(1).setACC(90).setEVD(5).setSPD(3).setSTR(
            11).setDEX(10).setCON(11).setINT(4).setWIS(5).setCHA(2).setHP(15).resetHP()
        # Initialize the moveset
        self.abilities.setAttack(ClawAttack(
            self, self.stats[Stat.ACC])).addUniqueSkill(RockThrow(self))

    def combatTurn(self, playerParty: Party, yourParty: Party):
        return super().combatTurn(playerParty, yourParty)


class ClawAttack(CombatAbility):

    def __init__(self, user: Monster, acc: int) -> None:
        super().__init__(user)
        self.name = 'Claw Attack'
        self.description = ''
        self.range = Range.CLOSE
        self.accuracy = acc

    def execute(self, target: Creature) -> None:
        if target is not None and type(target) is Character:
            dmg = max(1, target.stats[Stat.DEF] /
                      2 - self.user.stats[Stat.ATK])
            if doesHit(self.accuracy, target):
                print('{0} hit {1} dealing {2} Damage'.format(
                    self.user.getName(), target.getName(), dmg))
                target.setCurrentHP(max(0, target.getCurrentHP() - dmg))
                return
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
        self.accuracy = 85

    def execute(self, target: Creature) -> None:
        if target is not None and type(target) is Character:
            dmg = max(1, target.stats[Stat.DEF] /
                      2 - self.user.stats[Stat.ATK])
            if doesHit(self.accuracy, target):
                print('{0} hit {1} dealing {2} Damage'.format(
                    self.user.getName(), target.getName(), dmg))
                target.setCurrentHP(max(0, target.getCurrentHP() - dmg))
                return
            else:
                print('{0} missed {1}'.format(
                    self.user.getName(), target.getName()))
        print("No Target Specifed")
