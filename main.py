from __future__ import annotations

from entites.characters.character import Character
from entites.items import ShortBow, Spear, Staff, Sword
from entites.items.equipment import EquipentSlot
from entites.monsters.goblin import Goblin
from scenes.combat import Combat
from systems.party import Party, PartyRow


def game():
    # Create some characters
    warrior = Character().setName('Mark').equip(EquipentSlot.MAIN_HAND, Sword()).setSTR(15).setDEX(12).setCON(
        14).setINT(13).setWIS(10).setCHA(8).setHP(35).updateStats().resetHP()
    print(warrior.getStatBlock())
    rouge = Character().setName('Zefer').equip(EquipentSlot.MAIN_HAND, Sword()).setSTR(12).setDEX(15).setCON(
        13).setINT(10).setWIS(8).setCHA(14).setHP(20).updateStats().resetHP()
    print(rouge.getStatBlock())
    mage = Character().setName('Conrad').equip(EquipentSlot.MAIN_HAND, Staff()).setSTR(8).setDEX(10).setCON(
        13).setINT(15).setWIS(14).setCHA(12).setHP(20).updateStats().resetHP()
    print(mage.getStatBlock())
    cleric = Character().setName('Simic').equip(EquipentSlot.MAIN_HAND, Spear()).setSTR(13).setDEX(10).setCON(
        15).setINT(8).setWIS(14).setCHA(12).setHP(40).updateStats().resetHP()
    print(cleric.getStatBlock())
    ranger = Character().setName('Luna').equip(EquipentSlot.MAIN_HAND, ShortBow()).setSTR(10).setDEX(15).setCON(
        14).setINT(8).setWIS(12).setCHA(13).setHP(30).updateStats().resetHP()
    print(ranger.getStatBlock())

    # Create the Party
    player = Party().addToParty(warrior, PartyRow.FRONT).addToParty(rouge, PartyRow.FRONT).addToParty(
        mage, PartyRow.BACK).addToParty(cleric, PartyRow.FRONT).addToParty(ranger, PartyRow.BACK)

    # Create some monsters
    g1 = Goblin().setName('Goblin 1')
    g2 = Goblin().setName('Goblin 2')
    g3 = Goblin().setName('Goblin 3')

    emeny = Party().addToParty(g1, PartyRow.FRONT).addToParty(
        g2, PartyRow.FRONT).addToParty(g3, PartyRow.BACK)

    combatScene = Combat().setup(player, emeny)
    while combatScene.running():
        combatScene.run()


if __name__ == "__main__":
    game()
