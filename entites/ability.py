from __future__ import annotations

from enum import Enum
from typing import Any, overload

from entites.creature import Creature
from systems.party import Party


class Ability(object):

    def __init__(self, user: Any) -> None:
        self.name = ''
        self.description = ''
        self.user = user
        self.targetType = TargetType.SELF
        self.range = Range.SELF

    def setUser(self, user: Creature):
        self.user = user

    @overload
    def execute(self, target: Any) -> None:
        pass

    # Targeting logic
    def isTargetInRange(user: Creature, userParty: Party, target: Creature, targetParty: Party, range: Range) -> bool:
        if range is Range.SELF and user is target:
            return True
        if range is Range.CLOSE and userParty.isMemberInFront(user) and targetParty.isMemberInFront(target):
            return True
        if range is Range.VOLLY:
            if userParty.isMemberInFront(user) and targetParty.isMemberInBack(target):
                return True
            if userParty.isMemberInBack(user) and targetParty.isMemberInFront(target):
                return True
        if range is Range.REACH:
            if userParty.isMemberInFront(user):
                return True
            if userParty.isMemberInBack(user) and targetParty.isMemberInFront(target):
                return True
        if range in [Range.BACK, Range.BACKROW] and targetParty.isMemberInBack(target):
            return True
        if range in [Range.FRONT, Range.FRONTROW] and targetParty.isMemberInFront(target):
            return True
        if range is Range.SAMEROW and userParty.getMembersRow(user) is targetParty.getMembersRow(target):
            return True
        if range is Range.ALL:
            return True
        return False


class TargetType(Enum):
    SELF = 0
    ENEMY = 1
    ALLY = 2
    ENEMIES = 3
    ALLIES = 4


class Range(Enum):
    SELF = 0
    CLOSE = 1
    VOLLY = 2
    REACH = 3
    SAMEROW = 10
    ANYROW = 9
    FRONT = 4
    FRONTROW = 7
    BACK = 5
    BACKROW = 8
    ALL = 6


class AbilitySet(object):

    def __init__(self) -> None:
        self.attack = None
        self.uniqueLabel = ''
        self.unique = set()
        self.skills = dict()
        self.defense = set()

    def setAttack(self, attack: Ability) -> AbilitySet:
        self.attack = attack
        return self

    def setUniqueLabel(self, label: str) -> AbilitySet:
        self.uniqueLabel = label
        return self

    def addUniqueSkill(self, ability: Ability) -> AbilitySet:
        self.unique.add(ability)
        return self

    def addSkill(self, skillType: str, skill: Ability) -> AbilitySet:
        if skillType in self.skills.keys:
            self.skills[skillType].add(skill)
        else:
            skillSet = set([skill])
            self.skills[skillType] = skillSet
        return self

    def addDefensiveSkill(self, ability: Ability) -> AbilitySet:
        self.defense.add(ability)
        return self


class CombatAbility(Ability):

    def __init__(self, user: Any) -> None:
        super().__init__(user)
        self.targetType = TargetType.ENEMY

class FeildAbility(Ability):

    def __init__(self, user: Any) -> None:
        super().__init__(user)
        self.targetType = None


class SupportAbility(Ability):

    def __init__(self, user: Any) -> None:
        super().__init__(user)
        self.targetType = TargetType.ALLY


class DefenseAbility(Ability):

    def __init__(self, user: Any) -> None:
        super().__init__(user)
        self.targetType = TargetType.SELF
