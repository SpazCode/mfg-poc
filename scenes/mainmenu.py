from __future__ import annotations

import pygame
from pygame import Color, Rect
from config import getAssetPath
from scenes.scene import Scene
from ui.components.backgrounds import verticalGradientRect


class MainMenuScene(Scene):

    def setup(self) -> Scene:
        return super().setup()

    def render(self) -> None:
        background = Rect(0, 0, 640, 400)
        verticalGradientRect(self._display_surface, Color(
            168, 58, 34), Color(168, 125, 34), background)
        logo_img = pygame.image.load(getAssetPath("logo.PNG"))
        self._display_surface.blit(background)
        self._display_surface.blit(logo_img)
