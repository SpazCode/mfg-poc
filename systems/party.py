from __future__ import annotations

from enum import Enum
from entites.creature import Creature


class Party(object):

    def __init__(self) -> None:
        self.members = list()
        self.rows = {PartyRow.FRONT: [None, None, None],
                     PartyRow.BACK: [None, None, None]}
        self.sizeLimit = 11

    def changeLine(self, charaIndex: int) -> Party:
        frm = ''
        to = ''
        if charaIndex in self.rows[PartyRow.FRONT]:
            frm = PartyRow.FRONT
            to = PartyRow.BACK
        else:
            to = PartyRow.FRONT
            frm = PartyRow.BACK

        if self.rows[to].contains(None):
            self.rows[frm].remove(charaIndex)
            self.rows[frm].append(None)
            self.rows[frm].append(charaIndex)
            self.rows[frm].remove(None)

        return self

    def addToParty(self, creature: Creature, row: PartyRow) -> Party:
        if sum(list(map(lambda c: int(c.size),  self.members))) < self.sizeLimit:
            if None in self.rows[row]:
                self.rows[row].remove(None)
                self.members.append(creature)
                self.rows[row].append(self.members.index(creature))
            else:
                raise PartyAdditionError('The row was already full.')
        else:
            raise PartyAdditionError('This party is already full.')
        return self

    def __str__(self) -> str:
        output = 'Front: '
        for member in self.rows[PartyRow.FRONT]:
            if member is not None:
                output += self._formatChracterOutput(self.members[member])
        output += ' - Back: '
        for member in self.rows[PartyRow.BACK]:
            if member is not None:
                output += self._formatChracterOutput(self.members[member])

        return output

    def _formatChracterOutput(self, creature: Creature) -> str:
        return '|' + creature.getName() + ' - HP:' + str(creature.getCurrentHP()) + '/' + str(creature.getHP()) + '|'


class PartyAdditionError(Exception):
    pass


class PartyRow(Enum):
    FRONT = 1
    BACK = 2
