from __future__ import annotations

from enum import Enum

class Stats(dict):
    def __init__(self, *args, **kwargs):
        self.setDefaults()
        self.update(*args, **kwargs)

    def __getitem__(self, key: Stat):
        val = dict.__getitem__(self, key)
        return val

    def __setitem__(self, key: Stat, val: int):
        if type(key) is not Stat:
            raise Exception('Only a Stat can be included')
        dict.__setitem__(self, key, val)

    def __repr__(self):
        dictrepr = dict.__repr__(self)
        return '%s(%s)' % (type(self).__name__, dictrepr)
        
    def update(self, *args, **kwargs):
        for k, v in dict(*args, **kwargs).items():
            self[k] = v

    def setDefaults(self):
        self.__setitem__(Stat.ATK, 0)
        self.__setitem__(Stat.DEF, 1)
        self.__setitem__(Stat.MAG, 0)
        self.__setitem__(Stat.RES, 0)
        self.__setitem__(Stat.EVD, 50)
        self.__setitem__(Stat.ACC, 0)
        self.__setitem__(Stat.SPD, 5)

class Stat(Enum):
    ATK = 1
    DEF = 2
    MAG = 3
    RES = 4
    EVD = 5
    ACC = 6
    SPD = 7
