from __future__ import annotations

from systems.inputs import InputManager


class Scene(object):
    def __init__(self, surface, input_manager: InputManager) -> None:
        self.ongoing = False
        self._display_surface = surface
        self._input_manager = input_manager

    # initialize the scene and it's variables
    def setup(self) -> Scene:
        return self

    # Update the scene logic before rendering
    def update(self) -> None:
        pass

    # Render the scene based on the curernt game state
    def render(self) -> None:
        pass

    # Allows you to check if the scene is still running
    def running(self) -> bool:
        return self.ongoing

    # End and clean up the scene
    def end(self) -> None:
        pass
