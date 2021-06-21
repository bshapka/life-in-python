from typing import List, Tuple
import pygame
from life.World import World
import random as rand


class Game:
    """
    Represents an instance of Conway's Game of Life

    Fields:
        world: World
            An instance of World with a state and a method to transition to the next state

        cell_size: int
            The size (size == length == width) of a rendered cell

    Methods:
        play() -> None
            Plays the game by rendering each state of the World on a Pygame surface
            until the user closes the game window
    """
    def __init__(self, cell_size: int, initial_state: List[List[bool]] = None) -> None:
        """
        Instantiates a Game

        :param cell_size: the size of each cell in pixels

        :param initial_state: an initial state for a World

        :returns None
        """
        self.__validate_cell_size(cell_size)
        self.cell_size = cell_size
        if initial_state is not None:
            self.__validate_state(initial_state, cell_size)
            self.world = World(initial_state)
        else:
            random_state = Game.__get_random_state(cell_size, 10)
            self.world = World(random_state)

    @staticmethod
    def __get_screen_dimensions() -> Tuple[int, int]:
        """
        Returns screen dimensions in pixels as a tuple of form (width, height)

        :returns screen dimensions in pixels as a tuple of form (width, height)
        """
        pygame.init()
        dimensions = (pygame.display.Info().current_w, pygame.display.Info().current_h)
        pygame.quit()
        return dimensions

    @staticmethod
    def __validate_cell_size(cell_size: int) -> None:
        """
        Validates a given cell_size

        :raises ValueError if cell_size is too big for screen or cell_size is negative

        :param cell_size: the size of each cell in pixels

        :returns None
        """
        if cell_size < 0:
            raise ValueError("The cell_size cannot be negative.")

        screen_dimensions = Game.__get_screen_dimensions()
        cell_is_too_big = any(d for d in screen_dimensions if cell_size > d)
        if cell_is_too_big:
            raise ValueError("The cell_size must not exceed any of the screen's dimensions.")

    @staticmethod
    def __validate_state(state: List[List[bool]], cell_size: int) -> None:
        """
        Validates a given state and cell_size combination

        :raises ValueError if state dimensions scaled by cell_size are too big for the screen

        :param state: an initial state for a World

        :param cell_size: the size of each cell in pixels

        :returns None
        """
        screen_width, screen_height = Game.__get_screen_dimensions()
        state_dimensions = World(state).get_dimensions()
        scaled_state_length, scaled_state_width = (dim * cell_size for dim in state_dimensions)

        if scaled_state_length > screen_width:
            raise ValueError("The product of the length of the state and cell_size cannot exceed the screen's width")

        if scaled_state_width > screen_height:
            raise ValueError("The product of the width of the state and cell_size cannot exceed the screen's height")

    @staticmethod
    def __get_random_state(cell_size: int, sample_size: int) -> List[List[bool]]:
        """
        Returns a random state scaled to fill the screen

        Every cell in the state has a 1 / sample_size probability of being live,
        and therefore a (sample_size - 1) / sample_size probability of being dead.

        The state will be constructed using cell_size and the screen size so that
        the state will fill the screen when rendered

        :param cell_size: the size of each cell in pixels

        :param sample_size: the size of the sample from which live/dead cells are drawn

        :returns: a random state scaled to fill the screen
        """
        screen_dimensions = Game.__get_screen_dimensions()
        length, width = (dim // cell_size for dim in screen_dimensions)

        def rand_bool() -> bool:
            """
            Returns a random bool

            The bool will be true with 1 / sample_size probability and false with
            a (sample_size - 1) / sample_size probability.

            :return: a random bool
            """
            return not bool(rand.randrange(0, sample_size))

        state = [[rand_bool() for j in range(length)] for i in range(width)]
        return state

    def play(self) -> None:
        """
        Plays Conway's Game of Life

        Renders each state of the World associated with self on a Pygame surface.
        Continues doing this until the user closes the game window

        :returns None
        """
        pygame.init()
        screen_dimensions = Game.__get_screen_dimensions()
        surface = pygame.display.set_mode(screen_dimensions, pygame.FULLSCREEN)
        colours = {'white': (255,) * 3, 'green': (0, 255, 0)}
        while not pygame.event.get(pygame.QUIT):
            surface.fill(colours['white'])
            length, width = self.world.get_dimensions()
            state = self.world.get_state()
            for row_index in range(width):
                state_row = state[row_index]
                for col_index, is_live in enumerate(state_row):
                    if is_live:
                        position = (col_index * self.cell_size, row_index * self.cell_size)
                        cell = pygame.Rect(position, (self.cell_size,) * 2)
                        pygame.draw.rect(surface, colours['green'], cell)
            pygame.display.flip()
            self.world.next_state()
        pygame.quit()

