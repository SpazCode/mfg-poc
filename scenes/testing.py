from __future__ import annotations

import pygame
from pygame import Color, Rect
from pygame.font import Font
from config import getAssetPath
from scenes.scene import Scene
from systems.inputs import InputCommand
from ui.components.backgrounds import verticalGradientRect
from ui.utilities import x_center


class TestingScene(Scene):
    __MAX_INPUT_DELAY = 25

    def setup(self) -> Scene:
        self.menu_index = 0
        self.input_pause = TestingScene.__MAX_INPUT_DELAY
        self.menu_options = ['New Game', 'Continue', 'Quit Game']
        if not pygame.font.get_init():
            raise FontError("Fonts were not initialized")
        self.text_font = Font(getAssetPath(
            "fonts/PixelAzureBonds-327Z.ttf"), 20)
        return super().setup()

    def update(self) -> None:
        if self.input_pause >= TestingScene.__MAX_INPUT_DELAY:
            if self._input_manager.is_pressed(InputCommand.UP):
                self.menu_index = max(0, self.menu_index - 1)
            if self._input_manager.is_pressed(InputCommand.DOWN):
                self.menu_index = min(
                    len(self.menu_options) - 1, self.menu_index + 1)
        else:
            self.input_pause = min(
                TestingScene.__MAX_INPUT_DELAY, self.input_pause + 1)

    def render(self) -> None:
        background = Rect(0, 0, 640, 400)
        verticalGradientRect(self._display_surface, Color(
            168, 58, 34), Color(168, 125, 34), background)
        logo_img = pygame.image.load(getAssetPath("logo.PNG"))
        # Set up the logo
        logo_size = (int(logo_img.get_width() * 0.62),
                     int(logo_img.get_height() * 0.62))
        logo_img = pygame.transform.scale(logo_img, logo_size)
        center_x = x_center(self._display_surface.get_width(), logo_size[0])
        self._display_surface.blit(logo_img, (center_x, 0))
        # Create the menu options
        opt_y = logo_img.get_height() + 25
        for i, opt in enumerate(self.menu_options):
            background = None if self.menu_index is not i else Color(
                255, 255, 255, 50)
            opt_surface = self.text_font.render(
                opt, False, Color(0, 0, 0), background)
            cx = x_center(self._display_surface.get_width(),
                          opt_surface.get_width())
            self._display_surface.blit(opt_surface, (cx, opt_y))
            opt_y += 10 + opt_surface.get_height()


class FontError(Exception):
    pass
