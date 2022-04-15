from __future__ import annotations

from pygame import Surface
from ui.components.components import Component


class Container(Component):
    """ Housing to manage a group of components in the game """

    def __init__(self) -> None:
        self._components = dict()
        self._order = list()
        super().__init__()

    def on_render(self) -> Surface:
        surface = Surface((self._w, self._h))
        for id in self._order:
            com_surface = self._components[id].on_render()
            surface.blit(
                com_surface, (self._components[id].get_x(), self._components[id].get_y()))
        return surface

    def on_update(self) -> None:
        for id in self._order:
            self._components[id].on_update()

    def add_component(self, id: str, component: Component) -> Container:
        component.initialize()
        self._order.append(id)
        self._components[id] = component

    def remove_component(self, id: str) -> Container:
        self._order.remove(id)
        del self._components[id]
        return self

    def get_components(self) -> list:
        return self._order

    def move_component_forward(self, id: str) -> Container:
        self._check_id(id)
        index = self._order.index(id)
        if index > 0:
            rep = self._order[index - 1]
            self._order[index - 1] = self._order[index]
            self._order[index] = rep
        return self

    def move_component_back(self, id: str) -> Container:
        self._check_id(id)
        index = self._order.index(id)
        if index < len(self._order) - 1:
            rep = self._order[index + 1]
            self._order[index + 1] = self._order[index]
            self._order[index] = rep
        return self

    def send_to_front(self, id: str) -> Container:
        self._check_id(id)
        index = self._order.index(id)
        rep = self._order[0]
        self._order[0] = self._order[index]
        self._order[index] = rep
        return self

    def send_to_back(self, id: str) -> Container:
        self._check_id(id)
        index = self._order.index(id)
        rep = self._order[len(self._order) - 1]
        self._order[len(self._order) - 1] = self._order[index]
        self._order[index] = rep
        return self

    def _check_id(self, id: str):
        if id not in self._order:
            raise Container.NoIdException(
                '{0} is not in the component'.format(id))

    class NoIdException(Exception):
        pass
