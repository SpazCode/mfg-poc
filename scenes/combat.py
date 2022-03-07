from __future__ import annotations

from collections import deque
from random import randint
from typing import Any
from entites.ability import Range, TargetType
from entites.characters.character import AbilitySet, Character
from entites.creature import Creature
from entites.monsters.monster import Monster
from .scene import Scene
from systems.party import Party, PartyRow


class Combat(Scene):

    def __init__(self) -> None:
        super().__init__()
        self.playerParty = Party()
        self.enemyParty = Party()
        self.turnOrder = list()

    def setup(self, player: Party, enemy: Party) -> Scene:
        # Setup the parties
        self.playerParty = player
        self.enemyParty = enemy
        self.ongoing = True
        # Create turn order
        creaturesInCombat = [c for c in player.members if c is not None] + \
            [c for c in enemy.members if c is not None]
        creaturesInCombat = list(
            map(lambda c: (c,  int(c.SPD)), creaturesInCombat))
        creaturesInCombat.sort(key=lambda p: p[1], reverse=True)
        self.turnOrder = deque(list(map(lambda p: p[0], creaturesInCombat)))
        return self

    def run(self) -> None:
        print('===============================')
        print(str(self.playerParty))
        print(' < VS > ')
        print(str(self.enemyParty))

        print(' '.join(list(map(lambda x: str(x), self.turnOrder))))
        current = self.turnOrder.popleft()
        if current in self.playerParty.members:
            self.playerCommand(current)
        else:
            self.enemyCommand(current)
        self.turnOrder.append(current)
        print('===============================')

    def playerCommand(self, curr: Character) -> None:
        print('-------------------------------')
        print('It is the ' + curr.getName() + ' turn')
        print('-------------------------------')
        inMenu = True
        ability = curr.abilities
        while inMenu:
            print('|-----------------------------|')
            chooser = self.buildPlayerMenu(ability)
            print('-------------------------------')
            command = input("Enter Command: ")
            choice = chooser[command]
            ability = choice[0]
            inMenu = choice[1]

            # We end the combat if there is no abilty chosen and we want to leave the menu
            # This is most likely an escape attempt
            if not inMenu and ability is None:
                self.end()

            # We move on to the trageting if we can.
            target = None
            if not inMenu and ability is not None:
                print('<----------------------------->')
                if ability.targetType == TargetType.SELF:
                    target = curr
                else:
                    targetChooser = {}
                    # If we need to traget a Character then we target Each Memeber
                    if ability.targetType == TargetType.ALLY:
                        for i, m in enumerate(self.playerParty.members):
                            print('({0}) - {1}'.format(i, m.name))
                            targetChooser[str(i)] = m
                    elif ability.targetType == TargetType.ENEMY:
                        for i, m in enumerate(self.enemyParty.members):
                            print('({0}) - {1}'.format(i, m.name))
                            targetChooser[str(i)] = m
                    print('(R)estart')
                    command = input("Choose a Target: ")
                    target = targetChooser[command]

            # Restart the Menus
            if command in ['r', 'R']:
                inMenu = True
                ability = curr.abilities

            # Execute the command on the traget
            if target is not None:
                ability.execute(target)

    def buildPlayerMenu(self, abilities: Any) -> dict:
        # Top level menu for the player
        abilityChooser = {}
        if type(abilities) is AbilitySet:
            print('(A)ttack')
            print('(D)efense')
            print('(S)kills')
            if len(abilities.unique) > 1:
                print('(U):{0}'.format(abilities.uniqueLabel))
            print('(E)scape')
            # Build the ability chooser
            abilityChooser['a'] = abilityChooser['A'] = (
                abilities.attack, False)
            abilityChooser['d'] = abilityChooser['D'] = (
                abilities.defense, True)
            abilityChooser['s'] = abilityChooser['S'] = (
                abilities.skills, True)
            abilityChooser['u'] = abilityChooser['U'] = (
                abilities.unique, True)
            abilityChooser['e'] = abilityChooser['E'] = (None, False)
            return abilityChooser
        # if we are passed the set of abilities then we itterate through them and build a chooser for them.
        if type(abilities) is set:
            for i, a in enumerate(abilities):
                print('({0}) - {1}'.format(i, a.name))
                abilityChooser[str(i)] = (a, False)
            print('(R)estart')
            abilityChooser['r'] = abilityChooser['R'] = (None, True)
            return abilityChooser
        # if we pass a dict of differnt ability types then we build the sub menu
        if type(abilities) is dict:
            for i, n in enumerate(abilities.keys()):
                print('({0}) - {1}'.format(i, n))
                abilityChooser[str(i)] = (abilities[n], False)
            print('(R)estart')
            abilityChooser['r'] = abilityChooser['R'] = (None, True)
            return abilityChooser

    def enemyCommand(self, curr: Monster) -> None:
        ability = None
        if len(curr.abilities.unique) > 1:
            choice = randint(-1, len(curr.abilities.unique) -1)
            if choice == -1:
                ability = curr.abilities.attack
            else:
                ability = curr.abilities.unique[choice]
        else:
            ability = curr.abilities.attack

        if ability == None:
            return

        target = None
        if ability.targetType == TargetType.ENEMY:
            targetIndex = randint(0, len(self.playerParty.members) - 1)
            target = self.playerParty.members[targetIndex]

        ability.execute(target)

    # Targeting System
    def isTargetInRange(self, user: Creature, userParty:Party, target: Creature, targetParty: Party, range: Range) -> bool:
        if range is Range.SELF and user is target:
            return True
        if range is Range.CLOSE and user in userParty.rows[PartyRow.FRONT] and target in targetParty.rows[PartyRow.FRONT]:
            return True
        if range is Range.VOLLY:
            if user in userParty.rows[PartyRow.FRONT] and target in targetParty.rows[PartyRow.BACK]:
                return True
            if user in userParty.rows[PartyRow.BACK] and target in targetParty.rows[PartyRow.FRONT]:
                return True
        if range is Range.REACH:
            if user in userParty.rows[PartyRow.FRONT]:
                return True
            if user in userParty.rows[PartyRow.BACK] and target in targetParty.rows[PartyRow.FRONT]:
                return True
        if range in [Range.BACK, Range.BACKROW] and target in targetParty.rows[PartyRow.BACK]:
            return True
        if range in [Range.FRONT, Range.FRONTROW] and target in targetParty.rows[PartyRow.FRONT]:
            return True
        if range is Range.ALL:
            return True            
        return False


    def end(self) -> None:
        print('Ending Combat')
        self.ongoing = False
