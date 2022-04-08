from __future__ import annotations

from pygame import Surface
from systems.inputs import InputManager
from ui.components.containers import Container


class Scene(object):
    """ Object to represent the scene being shown on the screen """

    def __init__(self, screen: Surface, input_manager: InputManager, scene_manager: SceneManager) -> None:
        self.ongoing = False
        self._screen = screen
        self._input_manager = input_manager
        self._scene_manager = scene_manager
        self._component_root = Container()
        self._component_root.set_width(
            screen.get_width()).set_height(screen.get_height())

    def setup(self) -> Scene:
        """ Initialize the scene and it's variables """
        return self

    def update(self) -> None:
        """ Update the scene logic before rendering """
        self._component_root.on_update()

    def render(self) -> None:
        """ Render the scene based on the curernt game state """
        self._screen.blit(self._component_root.on_render(), (0, 0))

    def running(self) -> bool:
        """ Allows you to check if the scene is still running """
        return self.ongoing

    def end(self) -> None:
        """ End and clean up the scene """
        pass


class SceneManager(object):
    """ Utility Class used to manage the {Scenes} through out the game. """

    def __init__(self, screen: Surface, input_manager: InputManager, end_game_callback: function) -> None:
        self._scenes = dict()
        self._current_scene_name = ''
        self._current_scene = None
        self._screen = screen
        self._input_manager = input_manager
        self._end_game_callback = end_game_callback

    def add_scene(self, name: str, scene) -> SceneManager:
        self._scenes[name] = scene
        return self

    def get_scenes(self) -> list:
        return self._scenes.keys()

    def set_scene(self, name: str) -> None:
        if name not in self._scenes.keys():
            raise Exception('This scene is not in the scene loader.')
        if self._current_scene is not None:
            self._current_scene.end()
            del self._current_scene
        self._current_scene_name = name
        self._current_scene = self._scenes[name](
            self._screen, self._input_manager, self).setup()

    def get_scene(self) -> Scene:
        return self._current_scene

    def end_game(self) -> None:
        self._end_game_callback()
