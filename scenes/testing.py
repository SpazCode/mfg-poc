from __future__ import annotations

from pygame import Color, Rect
import pygame
from config import getAssetPath
from scenes.scene import Scene
from ui.components.backgrounds import verticalGradientRect

class TestingScene(Scene):
    
    def setup(self) -> Scene:
        return super().setup()

    def render(self) -> None:
        background = Rect(0, 0, 640, 400)
        verticalGradientRect(self._display_surface, Color(
            168, 58, 34), Color(168, 125, 34), background)
        logo_img = pygame.image.load(getAssetPath("logo.PNG"))
        logo_size = (int(logo_img.get_width() * 0.62), int(logo_img.get_height() * 0.62))
        logo_img = pygame.transform.scale(logo_img, logo_size)
        center_x = int(self._display_surface.get_width() - logo_size[0]) / 2
        self._display_surface.blit(logo_img, (center_x, 0))
