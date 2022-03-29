from __future__ import annotations

from entites.ability import AbilitySet
from entites.creature import Creature, CreatureSize
from entites.items import BareHanded, UnArmoured
from entites.items.equipment import EquipentSlot, Equipment, EquipmentSet
from entites.items.weapon import Weapon
from systems.stats import Stat, Stats


class Character(Creature):

    def __init__(self) -> None:
        super().__init__()
        self.name = ""
        self.stats = Stats()
        self.size = CreatureSize.MEDIUM
        self.abilities = AbilitySet()
        self.equipment = EquipmentSet().equip(EquipentSlot.MAIN_HAND,
                                              BareHanded()).equip(EquipentSlot.BODY, UnArmoured())

    def getName(self) -> str:
        return self.name

    def setName(self, value: str) -> Character:
        self.name = value
        return self

    def getAbilitySet(self) -> AbilitySet:
        return self.abilities

    def equip(self, slot: EquipentSlot, weapon: Equipment) -> Character:
        if slot in [EquipentSlot.ACCESSORY_1, EquipentSlot.ACCESSORY_2]:
            pass
        elif slot in [EquipentSlot.MAIN_HAND]:
            if not isinstance(weapon, Weapon):
                pass
            self.equipment[EquipentSlot.MAIN_HAND] = weapon
        elif slot in [EquipentSlot.OFF_HAND]:
            pass
        else:
            pass
        return self

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
        if type(self.equipment[EquipentSlot.MAIN_HAND]) is Weapon and type(self.equipment[EquipentSlot.RIGHT_HAND]) is Weapon:
            # TODO(Stuart): Make the double attack ability to replace this.
            self.abilities.setAttack(
                self.equipment[EquipentSlot.MAIN_HAND].getAttack())
        else:
            self.abilities.setAttack(
                self.equipment[EquipentSlot.MAIN_HAND].getAttack())
        # Get the skills from the equiment
        for slot in self.equipment.keys():
            if self.equipment[slot] is not None:
                self.equipment[slot].equip(self)
                for skill in self.equipment[slot].skills:
                    if skill.canUse(self.getAttributes()):
                        self.abilities.addSkill(skill.skillType, skill.skill)
        return self

    def getStatBlock(self) -> str:
        return 'Name: {0} - HP: {6}, ATK: {1}, DEF: {2}, MAG: {3}, RES: {4}, SPD: {5}'.format(self.name, self.stats[Stat.ATK], self.stats[Stat.DEF], self.stats[Stat.MAG], self.stats[Stat.RES], self.stats[Stat.SPD], self.HP)

    def __str__(self) -> str:
        return self.name
