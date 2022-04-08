from __future__ import annotations

from pygame import Surface


class Component(object):
    """ Base class for Component object in the game """

    def __init__(self) -> None:
        self._x = 0
        self._y = 0
        self._w = 0
        self._h = 0

    def initialize(self) -> None:
        pass

    def on_render(self) -> Surface:
        return None

    def on_update(self) -> None:
        pass

    def set_x(self, value: int) -> Component:
        self._x = value
        return self

    def set_y(self, value: int) -> Component:
        self._y = value
        return self

    def set_width(self, value: int) -> Component:
        self._w = value
        return self

    def set_height(self, value: int) -> Component:
        self._h = value
        return self

    def get_x(self) -> int:
        return self._x

    def get_y(self) -> int:
        return self._y

    def get_width(self) -> int:
        return self._w

    def get_height(self) -> int:
        return self._h
