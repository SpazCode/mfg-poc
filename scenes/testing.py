from __future__ import annotations
from os import symlink

from pygame import Color, Rect
from scenes.scene import Scene
from systems.inputs import InputCommand
from ui.components.backgrounds import GradientBackground, verticalGradientRect
from ui.components.buttons import Button
from ui.utilities import x_center, y_center


class TesterScene(Scene):
    __MAX_INPUT_DELAY = 25

    def setup(self) -> Scene:
        self.input_pause = TesterScene.__MAX_INPUT_DELAY
        bg = GradientBackground()
        bg.set_colors(Color(58, 168, 34), Color(125, 168, 34)).set_height(
            self._component_root.get_height()).set_width(self._component_root.get_width())
        self.add_component('bg', bg)
        button = Button()
        button.set_background_color(
            Color(255, 125, 125)).set_width(100).set_height(30)
        button.set_x(x_center(self._component_root.get_width(), button.get_width())).set_y(
            y_center(self._component_root.get_height(), button.get_height()))
        self.add_component('button', button)
        return super(Scene, self).setup()

    def update(self) -> None:
        if self.input_pause >= TesterScene.__MAX_INPUT_DELAY:
            if self._input_manager.is_pressed(InputCommand.ACCEPT):
                self._scene_manager.set_scene('main_menu')
        else:
            self.input_pause = min(
                TesterScene.__MAX_INPUT_DELAY, self.input_pause + 1)
        return super(Scene, self).update()
