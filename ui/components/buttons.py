from __future__ import annotations

import pygame
from pygame import Color, Surface
from pygame.font import Font
from ui.components.components import Component
from ui.components.containers import Container
from ui.utilities import x_center, y_center


class Button(Component):
    """ Button UI component """

    def __init__(self) -> None:
        self._background_color = None
        self._focus_color = None
        self._on_click = None
        self._in_focus = False
        self._x_margin = 0
        self._y_margin = 0
        super().__init__()

    def set_background_color(self, color: Color) -> Button:
        self._background_color = color
        return self

    def set_focus_color(self, color: Color) -> Button:
        self._focus_color = color
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
            surface.fill(self._focus_color)
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


class TextButton(Button):
    """ Text Button: A button that has text """

    def __init__(self) -> None:
        self._text = ""
        self._text_color = None
        self._font = None
        super().__init__()

    def set_text(self, text: str) -> TextButton:
        self._text = text
        return self

    def set_font(self, font: Font) -> TextButton:
        self._font = font
        return self

    def set_text_color(self, color: Color) -> TextButton:
        self._text_color = color
        return self

    def on_render(self) -> Surface:
        surface = super(Button, self).on_render()
        if self._text is not None and self._font is not None:
            surface = self._font.render(
                self._text, False, self._text_color, surface)
        return surface


class ButtonList(Container):
    """ Button List, a container to manage """

    def __init__(self) -> None:
        self._current_button = None
        self._in_focused = False
        super().__init__()

    def get_focus(self) -> bool:
        return self._in_focused

    def set_focus(self, focus: bool) -> None:
        if self._current_button is None:
            self._current_button = 0
        self._in_focused = focus

    def select_next_button(self, direction: int):
        self._components[self._order[self._current_button]].set_focus(False)
        if direction < 0:
            self._current_button = min(0, self._current_button + direction)
        if direction > 0:
            self._current_button = max(
                len(self._order) - 1, self._current_button + direction)
        self._components[self._order[self._current_button]].set_focus(True)

    def add_button(self, id: str, component: Component) -> ButtonList:
        self.add_component(id, component)
        return self

    def remove_button(self, id: str) -> ButtonList:
        self.remove_component(id)
        return self
