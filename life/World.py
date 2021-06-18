from typing import List, Tuple


class World:

    def __init__(self, initial_state: List[List[bool]]):
        """
        Instantiates a World

        :raises TypeError if starting_state contains a non-bool

        :raises ValueError if starting_state is a jagged array

        :param starting_state: represents an initial state of the World

        :returns a new World
        """
        self.__validate_state(initial_state)
        self.state = initial_state

    def __validate_state(self, state: List[List[bool]]):
        """
        Validates a given state

        :raises TypeError if starting_state contains a non-bool

        :raises ValueError if starting_state is a jagged array

        :param state: represents a state of the World

        :returns void
        """
        row_lengths = set()
        for row in state:
            row_length = 0
            for cell in row:
                row_length += 1
                if type(cell) is not bool:
                    raise TypeError(
                        "Argument state must be of type List[List[bool]].")
            if row_lengths != set() and row_length not in row_lengths:
                raise ValueError("Argument must not be a jagged array")
            else:
                row_lengths.add(row_length)

    def get_state(self) -> List[List[bool]]:
        """
        returns state

        :param none

        :returns state
        """
        return self.state

    def next_state(self):
        """
        Advances state one generation

        :param none

        :returns void
        """
        self.state = [
            [self.__next_cell((i, j), is_live) for j, is_live in enumerate(row)]
            for i, row in enumerate(self.state)
        ]

    def __next_cell(self, coordinate: Tuple[int, int], is_live: bool) -> bool:
        """
        Transitions cell with given coordinate to live or dead

        :param coordinate: an ordered pair of form (row index, column index) giving
        the coordinate of a cell in the state

        :param is_live: the state of the cell (True if live, False if dead)

        :returns next cell at given coordinate in state
        """
        live_neighbour_count = self.__live_neighbour_count(coordinate)
        stays_live = is_live and live_neighbour_count in {2, 3}
        is_born = not(is_live) and live_neighbour_count == 3
        return stays_live or is_born

    def __live_neighbour_count(self, coordinate: Tuple[int, int]) -> int:
        """
        Returns count of live neighbouring cells to cell with given coordinate

        :param coordinate: an ordered pair of form (row index, column index) giving
        the coordinate of a cell in the state

        :returns count of live neighbouring cells to cell with given coordinate
        """
        row_index, col_index = coordinate
        offsets = range(-1, 2)
        neighbours = [
            self.__get_cell((row_index + i, col_index + j))
            for i in offsets
            for j in offsets
            if not(row_index == col_index == 0)
            and self.__is_valid_coordinate((row_index + i, col_index + j))
        ]
        return sum(neighbours)

    def __is_valid_coordinate(self, coordinate: Tuple[int, int]) -> bool:
        return False

    def __get_cell(self, coordinate: Tuple[int, int]) -> bool:
        return False