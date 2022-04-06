from __future__ import annotations

import pygame
from pygame.locals import *
from entites.characters.character import Character
from entites.items import ShortBow, Spear, Staff, Sword
from entites.items.equipment import EquipentSlot
from entites.monsters.goblin import Goblin
from scenes.combat import Combat
from scenes.mainmenu import MainMenuScene
from scenes.scene import SceneManager
from scenes.testing import TesterScene
from systems.inputs import InputManager, InputCommand
from systems.party import Party, PartyRow


class MyFamilyGuild(object):

    def __init__(self) -> None:
        self._running = True
        self._display_surface = None
        self.size = self.weight, self.height = 640, 400
        self._scenes_manager = None
        # TODO(SpazCode): Remplace this
        self._game_state = dict()
        # Initialize the input manager with the default control settings.
        self.input_manager = InputManager().initialize({InputCommand.ACCEPT: pygame.K_a,
                                                        InputCommand.CANCEL: pygame.K_s,
                                                        InputCommand.MENU: pygame.K_q,
                                                        InputCommand.UP: pygame.K_UP,
                                                        InputCommand.DOWN: pygame.K_DOWN,
                                                        InputCommand.LEFT: pygame.K_LEFT,
                                                        InputCommand.RIGHT: pygame.K_RIGHT})

    def on_init(self) -> None:
        # initialize pygame
        pygame.init()
        pygame.font.init()
        self._display_surface = pygame.display.set_mode(
            self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        pygame.display.set_caption("My Family Guild - POC")
        # Initalize the Scene manager in the game
        self._scenes_manager = SceneManager(
            self._display_surface, self.input_manager, self.end_game)
        self._scenes_manager.add_scene('main_menu', MainMenuScene)
        self._scenes_manager.add_scene('tester', TesterScene)
        self._scenes_manager.set_scene('main_menu')
        # Set the game to be running
        self._running = True

    def end_game(self) -> None:
        self._running = False

    # Process the input events from pygame
    def on_event(self, event) -> None:
        self.input_manager.update_status(event)
        if event.type == pygame.QUIT:
            self._running = False

    # Update the game state based on the events.
    def on_loop(self) -> None:
        self._scenes_manager.get_scene().update()

    # Handle rendering the game
    def on_render(self) -> None:
        self._scenes_manager.get_scene().render()
        pygame.display.flip()

    # Final cleanup tasks for the game on exit
    def on_cleanup(self) -> None:
        pygame.font.quit()
        pygame.quit()

    # Main game loop
    def on_execute(self) -> None:
        if self.on_init() == False:
            self._running = False

        clock = pygame.time.Clock()

        while(self._running):
            self.input_manager.reset_status()
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
            clock.tick(30)
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
