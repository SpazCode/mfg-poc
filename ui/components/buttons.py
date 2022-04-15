from __future__ import annotations

import pygame
from pygame import Color, Surface
from ui.components.components import Component
from ui.utilities import x_center, y_center


class Button(Component):
    """ Button UI component """

    def __init__(self) -> None:
        self._background_color = None
        self._on_click = None
        self._in_focus = False
        self._x_margin = 0
        self._y_margin = 0
        super().__init__()

    def set_background_color(self, color: Color) -> Button:
        self._background_color = color
        return self

    def set_on_click(self, callback: function) -> Button:
        self._on_click = callback
        return self

    def set_focus(self, focus: bool) -> None:
        self._in_focus = focus

    def get_focus(self) -> bool:
        return self._in_focus

    def initialize(self) -> None:
        self._x_margin = max(1, int(self.get_width() * 0.05))
        self._y_margin = max(1, int(self.get_width() * 0.05))

    def on_render(self) -> Surface:
        surface = Surface((self._w, self._h), pygame.SRCALPHA)
        if self._in_focus:
            surface.fill(Color(255, 255, 255, 125))
        # Build the button Image Surface
        inner_surface = Surface(
            (self._w - self._x_margin, self._h - self._y_margin))
        inner_surface.fill(self._background_color)
        # Put the button image
        surface.blit(inner_surface, (x_center(surface.get_width(), inner_surface.get_width(
        )), y_center(surface.get_height(), inner_surface.get_height())))
        return surface

    def on_update(self) -> None:
        if self._on_click is not None:
            self._on_click()
