from __future__ import annotations

import pygame
from pygame import Color, Rect
from pygame.font import Font
from config import getAssetPath
from scenes.scene import Scene
from systems.inputs import InputCommand
from ui.components.backgrounds import GradientBackground, verticalGradientRect
from ui.components.buttons import ButtonList, TextButton
from ui.components.images import Image
from ui.utilities import x_center, y_center


class MainMenuScene(Scene):
    __MAX_INPUT_DELAY = 25

    def setup(self) -> Scene:
        self.menu_index = 0
        self.input_pause = MainMenuScene.__MAX_INPUT_DELAY
        self.menu_options = ['New Game', 'Continue', 'Quit Game']
        if not pygame.font.get_init():
            raise FontError("Fonts were not initialized")
        self.text_font = Font(getAssetPath(
            "fonts/PixelAzureBonds-327Z.ttf"), 20)
        # Set up the rendered components
        bg = GradientBackground()
        bg.set_colors(Color(168, 58, 34), Color(168, 125, 34)).set_height(
            self._component_root.get_height()).set_width(self._component_root.get_width())
        self.add_component('bg', bg)
        # Logo
        logo = Image()
        logo.set_file("logo.PNG").set_scale((0.62, 0.62))
        self.add_component('logo', logo)
        logo.set_x(x_center(self._screen.get_width(), logo.get_width()))
        # Option List
        button_list = ButtonList()
        button_list.set_height(50 * len(self.menu_options)).set_width(120)
        # Creating all the buttons
        for i, opt in enumerate(self.menu_options):
            txtbtn = TextButton()
            txtbtn.set_text(opt).set_font(self.text_font).set_text_color(Color(0, 0, 0, 125)).set_background_color(
                None).set_focus_color(Color(255, 255, 255, 50)).set_height(40).set_width(120).set_x(0).set_y(5 + i * 40)
            button_list.add_button(opt, txtbtn)
        self.add_component('options_menu', button_list)
        button_list.set_x(x_center(self._screen.get_width(), button_list.get_width())).set_y(
            logo.get_height() + 25)
        # Return updated scene
        return super().setup()

    def update(self) -> None:
        if self.input_pause >= MainMenuScene.__MAX_INPUT_DELAY:
            if self._input_manager.is_pressed(InputCommand.UP):
                self.menu_index = max(0, self.menu_index - 1)
            if self._input_manager.is_pressed(InputCommand.DOWN):
                self.menu_index = min(
                    len(self.menu_options) - 1, self.menu_index + 1)
            if self._input_manager.is_pressed(InputCommand.ACCEPT):
                if self.menu_index < len(self.menu_options) - 1:
                    self._scene_manager.set_scene('tester')
                else:
                    self._scene_manager.end_game()
        else:
            self.input_pause = min(
                MainMenuScene.__MAX_INPUT_DELAY, self.input_pause + 1)
        return super().update()

    def render(self) -> None:
        super().render()


class FontError(Exception):
    pass
