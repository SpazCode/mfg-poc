from __future__ import annotations

import pygame
from enum import Enum
from pygame.event import Event


class InputManager(object):

    def __init__(self) -> None:
        self.initialized = False
        self.input_mapper = dict()
        self.inv_input_mapper = dict()
        self.input_status = {i: False for i in InputCommand}

    # Initialize the input manager, loading the mapping between inputs commands and pygame events.
    def initialize(self, command_settings: dict) -> InputManager:
        for v, k in enumerate(command_settings):
            if type(k) is not InputCommand or type(v) is not int:
                raise Exception('The command settings is malformed.')
            self.input_mapper[k] = v
        self.inv_input_mapper = {v: k for k, v in command_settings.items()}
        self.initialized = True
        return self

    # Update the status for the event, if it is a input we are watching update the status to true.
    def update_status(self, event) -> None:
        if not self.initialized:
            raise Exception('The input manager has not been initialized.')
        if event.type == pygame.KEYDOWN:
            if event.key in self.inv_input_mapper.keys():
                self.input_status[self.inv_input_mapper[event.key]] = True

    # Return the status of the input command we care about.
    def is_pressed(self, input: InputCommand) -> bool:
        return self.input_status[input]

    # Reset the input status, this should  be done at the begining fo the game loop.
    def reset_status(self) -> None:
        self.input_status = {i: False for i in InputCommand}


# The different inputs that we care about.
class InputCommand(Enum):
    ACCEPT = 1
    CANCEL = 2
    MENU = 3
    UP = 4
    DOWN = 5
    LEFT = 6
    RIGHT = 7
