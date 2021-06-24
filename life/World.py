from typing import List, Tuple, Set


class World:
    """
    Represents a 2D world in grid form with each cell in the grid being live or dead (but not both)

    Fields:
        state: Set[Tuple[int, int]]
            represents the state of the world as a set of 2-integer tuples. Each element of the set
            gives the coordinates of a live cell in the grid. As such, the coordinates of dead cells
            are not part of the state.

    Methods:
        next_state() -> None
            updates state by applying the rules of the game

        get_state() -> Set[Tuple[int, int]]
            returns state
    """

    def __init__(self, initial_state: Set[Tuple[int, int]]) -> None:
        """
        Instantiates a World

        :param initial_state: an initial state of the World

        :returns None
        """
        World.__validate_state(initial_state)
        self.state = initial_state

    @staticmethod
    def __validate_state(state: Set[Tuple[int, int]]) -> None:
        """
        validates a given state

        checks that state is of type Set[Tuple[int, int]]

        :raises TypeError if state is not of type Set

        :raises TypeError if any element of state is not of type Tuple

        :raises TypeError if any element of any element of state is not not of type int

        :raises ValueError if any element of state is not not of size 2

        :param state: a state for the World

        :returns None
        """
        error_message = "The state must be of type Set[Tuple[int, int]]. "

        if type(state) is not set:
            error_message += "The collection used is not of type set."
            raise TypeError(error_message)

        for coordinate in state:
            if type(coordinate) is not tuple:
                error_message += "An element of the set is not a tuple."
                raise TypeError(error_message)
            size = 0
            for component in coordinate:
                if type(component) is not int:
                    error_message += "A tuple in the set contains an element that is not of type int."
                    raise TypeError(error_message)
                size += 1
            if size != 2:
                error_message += "A tuple in the set is not of size 2."
                raise ValueError(error_message)

    def get_state(self) -> Set[Tuple[int, int]]:
        """
        returns state

        :returns state
        """
        return self.state

    def next_state(self) -> None:
        """
        Updates state by applying the rules of the game to all elements of state

        :returns None
        """
        self.state = [
            [self.__next_cell((i, j), is_live) for j, is_live in enumerate(row)]
            for i, row in enumerate(self.state)
        ]

    def __live_neighbour_count(self, coordinate: Tuple[int, int]) -> int:
        """
        Returns count of live neighbouring cells to cell with given coordinate

        :param coordinate: a tuple of form (row index, column index) giving the coordinate of a
        cell in state

        :returns count of live neighbouring cells to cell with given coordinate
        """
        row_index, col_index = coordinate
        offsets = range(-1, 2)
        neighbours = [
            self.__get_cell((row_index + row_offset, col_index + col_offset))
            for row_offset in offsets for col_offset in offsets
            if not row_offset == col_offset == 0
        ]
        return sum(neighbours)
