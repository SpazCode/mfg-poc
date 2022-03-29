from __future__ import annotations

from pygame import Color
from scenes.scene import Scene

class TestingScene(Scene):
    
    def setup(self) -> Scene:
        return super().setup()

    def render(self) -> None:
        self._display_surface.fill(Color(100, 50, 50))