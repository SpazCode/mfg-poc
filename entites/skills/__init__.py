from entites.ability import CombatAbility, Range
from entites.creature import Creature
from entites.monsters.monster import Monster
from systems.combat import doesHit
from systems.stats import Stat


class CloseMeleeAttack(CombatAbility):
    def __init__(self, user: Creature, accuracy: int) -> None:
        super().__init__(user)
        self.name = 'Melee Attack'
        self.description = 'Straking with the main hand weapon'
        self.range = Range.CLOSE
        self.accuracy = accuracy

    def execute(self, target: Monster) -> None:
        if target is not None:
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
                return
        print("No Target Specifed")

class RangeMaleeAttack(CombatAbility):
    def __init__(self, user: Creature, accuracy: int) -> None:
        super().__init__(user)
        self.name = 'Range Attack'
        self.description = 'Making a ranged attack with your main hand weaepon'
        self.range = Range.REACH
        self.accuracy = accuracy

    def execute(self, target: Monster) -> None:
        if target is not None:
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
                return
        print("No Target Specifed")


class RangeMagicAttack(CombatAbility):
    def __init__(self, user: Creature, accuracy: int) -> None:
        super().__init__(user)
        self.name = 'Magic Attack'
        self.description = 'Making a ranged magic attack with your main hand weaepon'
        self.range = Range.REACH
        self.accuracy = accuracy

    def execute(self, target: Monster) -> None:
        if target is not None:
            dmg = max(1, target.stats[Stat.RES] /
                        2 - self.user.stats[Stat.MAG])
            if doesHit(self.accuracy, target):
                print('{0} hit {1} dealing {2} Damage'.format(
                    self.user.getName(), target.getName(), dmg))
                target.setCurrentHP(max(0, target.getCurrentHP() - dmg))
                return
            else:
                print('{0} missed {1}'.format(
                    self.user.getName(), target.getName()))
                return
        print("No Target Specifed")