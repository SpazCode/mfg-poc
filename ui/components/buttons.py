from __future__ import annotations

from pygame import Color, Surface
from ui.components.components import Component


class Button(Component):
    """ Button UI component """

    def __init__(self) -> None:
        self._background_color = None
        self._on_click = None
        super().__init__()

    def set_background_color(self, color: Color) -> Button:
        self._background_color = color
        return self

    def set_on_click(self, callback: function) -> Button:
        self._on_click = callback
        return self

    def on_render(self) -> Surface:
        surface = Surface((self._w, self._h))
        surface.fill(self._background_color)
        return surface

    def on_update(self) -> None:
        if self._on_click is not None:
            self._on_click()
