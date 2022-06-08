from __future__ import annotations

import pygame
from pygame import Surface
from config import getAssetPath
from ui.components.components import Component


class Image(Component):

    def __init__(self) -> None:
        self._image_filename = ''
        self._image_surface = None
        self._scale = (1.0, 1.0)
        super().__init__()

    def initialize(self) -> None:
        if self._image_filename is not '':
            self._image_surface = pygame.image.load(
                getAssetPath(self._image_filename))
            self._w = self._image_surface.get_width() * self._scale[0]
            self._h = self._image_surface.get_height() * self._scale[1]

    def set_file(self, name: str) -> Image:
        self._image_filename = name
        return self

    def set_scale(self, scale: tuple) -> Image:
        self._scale = scale
        return self

    def on_render(self) -> Surface:
        return pygame.transform.scale(self._image_surface, (self._w, self._h))
