from __future__ import annotations

from random import randint
from entites.ability import AbilitySet, CombatAbility, Range
from entites.creature import Creature, CreatureSize
from entites.items.equipment import EquipentSlots, EquipmentSet
from entites.items.weapon import BareHanded, Weapon
from systems.stats import Stat, Stats


class Character(Creature):

    def __init__(self) -> None:
        super().__init__()
        self.name = ""
        self.stats = Stats()
        self.size = CreatureSize.MEDIUM
        self.abilities = AbilitySet().setAttack(Character.BasicAttack(self))
        barehands = BareHanded()
        barehands.equip(self)
        self.equipment = EquipmentSet().equip(EquipentSlots.MAIN_HAND, barehands)

    def getName(self) -> str:
        return self.name

    def setName(self, value: str) -> Character:
        self.name = value
        return self

    def getAbilitySet(self) -> AbilitySet:
        return self.abilities

    def updateStats(self) -> Character:
        # Set Base stats for a character.
        self.stats.setDefaults()
        # Update stats based on equipment
        for key in self.equipment.keys():
            equipped = self.equipment[key]
            if equipped is not None:
                mods = equipped.modifyStats(self.getAttributes())
                for stat in mods.keys():
                    self.stats[stat] += mods[stat]
        # Set attacks based on weapon(s)
        if type(self.equipment[EquipentSlots.MAIN_HAND]) is Weapon and type(self.equipment[EquipentSlots.RIGHT_HAND]) is Weapon:
            # TODO(Stuart): Make the double attack ability to replace this.
            self.abilities.setAttack(
                self.equipment[EquipentSlots.MAIN_HAND].getAttack())
        else:
            self.abilities.setAttack(
                self.equipment[EquipentSlots.MAIN_HAND].getAttack())
        # Get the skills from the equiment
        for slot in self.equipment.keys():
            if self.equipment[slot] is not None:
                for skill in self.equipment[slot].skills:
                    if skill.canUse(self.getAttributes()):
                        self.abilities.addSkill(skill.skillType, skill.skill)
        return self

    def getStatBlock(self) -> str:
        return 'Name: {0} - HP: {6}, ATK: {1}, DEF: {2}, MAG: {3}, RES: {4}, SPD: {5}'.format(self.name, self.stats[Stat.ATK], self.stats[Stat.DEF], self.stats[Stat.MAG], self.stats[Stat.RES], self.stats[Stat.SPD], self.HP)

    def __str__(self) -> str:
        return self.name

    class BasicAttack(CombatAbility):

        def __init__(self, user: Character) -> None:
            super().__init__(user)
            self.name = 'Attack'
            self.description = 'Basic attack with your main weapon'
            self.range = Range.CLOSE

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
