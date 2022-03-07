from __future__ import annotations


class Scene(object):
    def __init__(self) -> None:
        self.ongoing = False

    def setup(self) -> Scene:
        pass

    def run(self) -> None:
        pass

    def running(self) -> bool:
        return self.ongoing

    def end(self) -> None:
        pass
