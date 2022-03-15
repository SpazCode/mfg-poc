from __future__ import annotations

class Item(object):
    
    def __init__(self) -> None:
        self.name = ""
        self.cost = 0.0
        self.weight = 0.0
        self.description = ""

    def getDisplayName(self) -> str:
        return self.name

    def getDisplayCost(self) -> float:
        return self.cost

    def getDisplayWeight(self) -> float:
        return self.weight

    def getFormatedDescription(self) -> str:
        return self.description
