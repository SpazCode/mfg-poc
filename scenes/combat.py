from __future__ import annotations

from collections import deque
from random import randint
from typing import Any
from entites.ability import Ability, Range, TargetType
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
           current.combatTurn(self.playerParty,  self.enemyParty)
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
            abilityChooser = self.buildPlayerMenu(ability)
            print('-------------------------------')
            command = None
            while command not in abilityChooser.keys():
                command = input("Enter Command: ")
            choice = abilityChooser[command]
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
                if ability.targetType is TargetType.SELF:
                    target = curr
                elif ability.targetType is TargetType.ALLIES and ability.range is not Range.ANYROW:
                    # Get all allies in Range
                    target = list(filter(lambda m: Ability.isTargetInRange(
                        curr, self.playerParty, m, self.playerParty, ability.range), self.playerParty.members))
                elif ability.targetType is TargetType.ENEMIES and ability.range is not Range.ANYROW:
                    target = list(filter(lambda m: Ability.isTargetInRange(
                        curr, self.playerParty, m, self.enemyParty, ability.range), self.enemyParty.members))
                else:
                    targetChooser = {}
                    # If we need to traget a Character then we target Each Memeber
                    if ability.targetType == TargetType.ALLY:
                        targetsInRange = list(filter(lambda m: Ability.isTargetInRange(
                            curr, self.playerParty, m, self.playerParty, ability.range), self.playerParty.members))
                        for i, m in enumerate(targetsInRange):
                            print('({0}) - {1}'.format(i, m.name))
                            targetChooser[str(i)] = m
                    elif ability.targetType == TargetType.ENEMY:
                        targetsInRange = list(filter(lambda m: Ability.isTargetInRange(
                            curr, self.playerParty, m, self.enemyParty, ability.range), self.enemyParty.members))
                        for i, m in enumerate(targetsInRange):
                            print('({0}) - {1}'.format(i, m.name))
                            targetChooser[str(i)] = m
                    elif ability.targetType is TargetType.ALLIES and ability.range is Range.ANYROW:
                        print('(F)ront Row')
                        targetChooser['f'] = targetChooser['F'] = self.playerParty.rows[PartyRow.FRONT]
                        print('(B)ack Row')
                        targetChooser['b'] = targetChooser['B'] = self.playerParty.rows[PartyRow.BACK]
                    elif ability.targetType is TargetType.ENEMIES and ability.range is Range.ANYROW:
                        print('(F)ront Row')
                        targetChooser['f'] = targetChooser['F'] = self.enemyParty.rows[PartyRow.FRONT]
                        print('(B)ack Row')
                        targetChooser['b'] = targetChooser['B'] = self.enemyParty.rows[PartyRow.BACK]
                    print('(R)estart')
                    command = None
                    if len(targetChooser.keys()) < 1:
                        print("No targets in range")
                        command = 'r'
                    else:
                        while command not in targetChooser.keys():
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

    def end(self) -> None:
        print('Ending Combat')
        self.ongoing = False
