import pygame


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
