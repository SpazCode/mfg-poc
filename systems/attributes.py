from __future__ import annotations

from enum import Enum


class Attributes(dict):
    def __init__(self, *args, **kwargs):
        self.__setitem__(Attribute.STR, 0)
        self.__setitem__(Attribute.DEX, 0)
        self.__setitem__(Attribute.CON, 0)
        self.__setitem__(Attribute.INT, 0)
        self.__setitem__(Attribute.WIS, 0)
        self.__setitem__(Attribute.CHA, 0)
        self.update(*args, **kwargs)

    def __getitem__(self, key: Attribute):
        val = dict.__getitem__(self, key)
        return val

    def __setitem__(self, key: Attribute, val: int):
        if type(key) is not Attribute:
            raise Exception('Only an Atrribute can be included')
        dict.__setitem__(self, key, val)

    def __repr__(self):
        dictrepr = dict.__repr__(self)
        return '%s(%s)' % (type(self).__name__, dictrepr)
        
    def update(self, *args, **kwargs):
        for k, v in dict(*args, **kwargs).iteritems():
            self[k] = v

    def getModifier(self, key: Attribute):
        att = dict.__getitem__(self, key)
        return int(att / 2) - 5


class Attribute(Enum):
    STR = 1
    DEX = 2
    CON = 3
    INT = 4
    WIS = 5
    CHA = 6
