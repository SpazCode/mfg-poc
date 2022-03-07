from __future__ import annotations

class Item(object):
    
    def __init__(self) -> None:
        self.name = ""
        self.cost = 0.0
        self.weight = 0.0
        self.description = ""

    def getName(self) -> str:
        return self.name

    def setName(self, value: str) -> Item:
        self.name = value
        return self

    def getCost(self) -> float:
        return self.cost

    def setCost(self, value: float) -> Item:
        self.cost = value
        return self

    def getWeight(self) -> float:
        return self.weight

    def setWeight(self, value: float) -> Item:
        self.weight = value
        return self

    def getDescription(self) -> str:
        return self.description

    def setDescription(self, value: str) -> Item:
        self.description = value
        return self