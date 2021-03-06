from __future__ import annotations

import pygame
from pygame.locals import *
from entites.characters.character import Character
from entites.items import ShortBow, Spear, Staff, Sword
from entites.items.equipment import EquipentSlot
from entites.monsters.goblin import Goblin
from scenes.combat import Combat
from scenes.testing import TestingScene
from systems.party import Party, PartyRow


class MyFamilyGuild(object):

    def __init__(self) -> None:
        self._running = True
        self._display_surface = None
        self.size = self.weight, self.height = 640, 400
        self._scenes = dict()
        self.current_scene = ''
        self._game_state = dict()

    def on_init(self) -> None:
        pygame.init()
        self._display_surface = pygame.display.set_mode(
            self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        self._scenes['testing'] = TestingScene(self._display_surface)
        self.current_scene = 'testing'

    # Process the input events from pygame
    def on_event(self, event) -> None:
        if event.type == pygame.QUIT:
            self._running = False

    # Update the game state based on the events.
    def on_loop(self) -> None:
        pass

    # Handle rendering the game
    def on_render(self) -> None:
        self._scenes[self.current_scene].render()
        pygame.display.flip()

    # Final cleanup tasks for the game on exit
    def on_cleanup(self) -> None:
        pygame.quit()

    # Main game loop
    def on_execute(self) -> None:
        if self.on_init() == False:
            self._running = False

        while(self._running):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()


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
    mfg = MyFamilyGuild()
    mfg.on_execute()
