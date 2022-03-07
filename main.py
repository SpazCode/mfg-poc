from __future__ import annotations

from entites.characters.character import Character
from entites.monsters.goblin import Goblin
from entites.monsters.monster import Monster
from scenes.combat import Combat
from systems.party import Party, PartyRow


def game():
    # Create some characters
    warrior = Character().setName('Mark').setSTR(15).setDEX(12).setCON(
        14).setINT(13).setWIS(10).setCHA(8).setHP(35).updateStats().resetHP()
    print(warrior.getStatBlock())
    rouge = Character().setName('Zefer').setSTR(12).setDEX(15).setCON(
        13).setINT(10).setWIS(8).setCHA(14).setHP(20).updateStats().resetHP()
    print(rouge.getStatBlock())
    mage = Character().setName('Conrad').setSTR(8).setDEX(10).setCON(
        13).setINT(15).setWIS(14).setCHA(12).setHP(20).updateStats().resetHP()
    print(mage.getStatBlock())
    cleric = Character().setName('Simic').setSTR(13).setDEX(10).setCON(
        15).setINT(8).setWIS(14).setCHA(12).setHP(40).updateStats().resetHP()
    print(cleric.getStatBlock())
    ranger = Character().setName('Luna').setSTR(10).setDEX(15).setCON(
        14).setINT(8).setWIS(12).setCHA(13).setHP(30).updateStats().resetHP()
    print(ranger.getStatBlock())

    # Create the Party
    player = Party().addToParty(warrior, PartyRow.FRONT).addToParty(rouge, PartyRow.FRONT).addToParty(
        mage, PartyRow.BACK).addToParty(cleric, PartyRow.FRONT).addToParty(ranger, PartyRow.BACK)

    # Create some monsters
    bat = Monster().setName('Bat 1').setSTR(10).setDEX(10).setCON(
        10).setINT(5).setWIS(5).setCHA(2).setHP(10).updateStats().resetHP()
    print(bat.getStatBlock())
    goblin = Goblin().setName('Goblin 1')
    print(goblin.getStatBlock())
    goblin2 = Goblin().setName('Goblin 2')
    print(goblin.getStatBlock())

    emeny = Party().addToParty(bat, PartyRow.FRONT).addToParty(
        goblin, PartyRow.FRONT).addToParty(goblin2, PartyRow.BACK)

    combatScene = Combat().setup(player, emeny)
    while combatScene.running():
        combatScene.run()


if __name__ == "__main__":
    game()
