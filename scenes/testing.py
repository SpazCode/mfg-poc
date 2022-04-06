from __future__ import annotations

from pygame import Color, Rect
from scenes.scene import Scene
from systems.inputs import InputCommand
from ui.components.backgrounds import verticalGradientRect


class TesterScene(Scene):
    __MAX_INPUT_DELAY = 25

    def setup(self) -> Scene:
        self.input_pause = TesterScene.__MAX_INPUT_DELAY
        return super().setup()

    def update(self) -> None:
        if self.input_pause >= TesterScene.__MAX_INPUT_DELAY:
            if self._input_manager.is_pressed(InputCommand.ACCEPT):
                self._scene_manager.set_scene('main_menu')
        else:
            self.input_pause = min(
                TesterScene.__MAX_INPUT_DELAY, self.input_pause + 1)

    def render(self) -> None:
        background = Rect(0, 0, 640, 400)
        verticalGradientRect(self._screen, Color(
            58, 168, 34), Color(125, 168, 34), background)
