from __future__ import annotations

import pygame
from pygame import Color, Surface
from ui.components.components import Component


def horizontalGradientRect(screen, l_colour, r_colour, target_rect) -> None:
    """ Draw a horizontal-gradient filled rectangle covering <target_rect> """
    # tiny! 2x2 bitmap
    colour_rect = pygame.Surface((2, 2))
    # left colour line
    pygame.draw.line(colour_rect, l_colour, (0, 0), (0, 1))
    # right colour line
    pygame.draw.line(colour_rect, r_colour, (1, 0), (1, 1))
    # stretch!
    colour_rect = pygame.transform.smoothscale(
        colour_rect, (target_rect.width, target_rect.height))
    # paint it
    screen.blit(colour_rect, target_rect)


def verticalGradientRect(screen, t_colour, b_colour, target_rect) -> None:
    """ Draw a vertial-gradient filled rectangle covering <target_rect> """
    # tiny! 2x2 bitmap
    colour_rect = pygame.Surface((2, 2))
    # top colour line
    pygame.draw.line(colour_rect, t_colour, (0, 0), (1, 0))
    # bottom colour line
    pygame.draw.line(colour_rect, b_colour, (0, 1), (1, 1))
    # stretch!
    colour_rect = pygame.transform.smoothscale(
        colour_rect, (target_rect.width, target_rect.height))
    # paint it
    screen.blit(colour_rect, target_rect)


class GradientBackground(Component):
    """ Compnent that is the container filling background that is a gradient"""

    def __init__(self) -> None:
        self._color_1 = None
        self._color_2 = None
        self._horizontal = False
        super().__init__()

    def set_colors(self, c1: Color, c2: Color) -> GradientBackground:
        self._color_1 = c1
        self._color_2 = c2
        return self

    def on_render(self) -> Surface:
        surface = Surface((self._w, self._h))
        if self._horizontal:
            surface.blit(GradientBackground._horizontalGradientRect(
                self._color_1, self._color_2, self._w, self._h), (self.get_x(), self.get_y()))
        else:
            surface.blit(GradientBackground._verticalGradientRect(
                self._color_1, self._color_2, self._w, self._h), (self.get_x(), self.get_y()))
        return surface

    def _horizontalGradientRect(l_colour, r_colour, w, h) -> Surface:
        """ Draw a horizontal-gradient filled rectangle covering <target_rect> """
        # tiny! 2x2 bitmap
        colour_rect = Surface((2, 2))
        # left colour line
        pygame.draw.line(colour_rect, l_colour, (0, 0), (0, 1))
        # right colour line
        pygame.draw.line(colour_rect, r_colour, (1, 0), (1, 1))
        # stretch!
        return pygame.transform.smoothscale(
            colour_rect, (w, h))

    def _verticalGradientRect(t_colour, b_colour, w, h) -> None:
        """ Draw a vertial-gradient filled rectangle covering <target_rect> """
        # tiny! 2x2 bitmap
        colour_rect = pygame.Surface((2, 2))
        # top colour line
        pygame.draw.line(colour_rect, t_colour, (0, 0), (1, 0))
        # bottom colour line
        pygame.draw.line(colour_rect, b_colour, (0, 1), (1, 1))
        # stretch!
        return pygame.transform.smoothscale(
            colour_rect, (w, h))


class SolidBackground(Component):
    """ Compnent that is the container filling background that is a gradient"""

    def __init__(self) -> None:
        self._background_color = None
        super().__init__()

    def set_background_color(self, color: Color) -> SolidBackground:
        self._background_color = color
        return self

    def on_render(self) -> Surface:
        surface = Surface((self._w, self._h))
        surface.fill(self._background_color)
        return surface
