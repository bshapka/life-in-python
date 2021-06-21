from typing import List, Tuple


class World:
    """
    Represents a 2D world with cells that are live or dead

    Fields:
        state: List[List[bool]]
            represents the state of the world as a 2D list of bool
            where True represents live and False represents dead

    Methods:
            advances state one generation

        get_state() -> List[List[bool]]
            returns state
    """

    def __init__(self, initial_state: List[List[bool]]) -> None:
        """
        Instantiates a World

        :param initial_state: represents an initial state of the World

        :returns None
        """
        World.__validate_state(initial_state)
        self.state = initial_state

    @staticmethod
    def __validate_state(state: List[List[bool]]) -> None:
        """
        Validates a given state

        Checks that state is of proper type and that state is not
        a jagged array

        :raises TypeError if state contains a non-bool

        :raises ValueError if state is a jagged array

        :param state: represents a state of the World

        :returns None
        """
        row_lengths = set()
        for row in state:
            row_length = 0
            for cell in row:
                row_length += 1
                if type(cell) is not bool:
                    raise TypeError(
                        "The state must be of type List[List[bool]].")
            if row_lengths != set() and row_length not in row_lengths:
                raise ValueError("The state must not be a jagged array")
            else:
                row_lengths.add(row_length)

    def get_state(self) -> List[List[bool]]:
        """
        returns state

        :returns state
        """
        return self.state

    def get_dimensions(self) -> Tuple[int, int]:
        """
        Returns the dimensions of the state as a tuple of form (length, width)

        assumes: state is not a jagged array

        :returns the dimensions of the state as a tuple of form (length, width)
        """
        dimensions = (0, 0)
        if self.state:
            dimensions = (len(self.state[0]), len(self.state))
        return dimensions

    def next_state(self) -> None:
        """
        Advances state one generation

        :returns void
        """
        self.state = [
            [self.__next_cell((i, j), is_live) for j, is_live in enumerate(row)]
            for i, row in enumerate(self.state)
        ]

    def __next_cell(self, coordinate: Tuple[int, int], is_live: bool) -> bool:
        """
        Transitions cell with given coordinate to live or dead

        :param coordinate: a tuple of form (row index, column index) giving
        the coordinate of a cell in the state

        :param is_live: the state of the cell (True if live, False if dead)

        :returns next cell at given coordinate in state
        """
        live_neighbour_count = self.__live_neighbour_count(coordinate)
        stays_live = is_live and live_neighbour_count in {2, 3}
        is_born = not is_live and live_neighbour_count == 3
        return stays_live or is_born

    def __live_neighbour_count(self, coordinate: Tuple[int, int]) -> int:
        """
        Returns count of live neighbouring cells to cell with given coordinate

        :param coordinate: a tuple of form (row index, column index) giving
        the coordinate of a cell in the state

        :returns count of live neighbouring cells to cell with given coordinate
        """
        row_index, col_index = coordinate
        offsets = range(-1, 2)
        neighbours = [
            self.__get_cell((row_index + row_offset, col_index + col_offset))
            for row_offset in offsets
            for col_offset in offsets
            if not(row_offset == col_offset == 0)
            and self.__is_valid_coordinate((row_index + row_offset, col_index + col_offset))
        ]
        return sum(neighbours)

    def __is_valid_coordinate(self, coordinate: Tuple[int, int]) -> bool:
        """
        Returns true if given coordinate is within state, else returns false

        :param coordinate: a tuple of form (row index, column index) giving
        the coordinate of a cell in the state

        :returns true if given coordinate is within state, else returns false
        """
        min_row_index = min_col_index = 0
        length, width = self.get_dimensions()
        max_row_index, max_col_index = width - 1, length - 1

        row_index, col_index = coordinate
        is_valid_row_index = min_row_index <= row_index <= max_row_index
        is_valid_col_index = min_col_index <= col_index <= max_col_index
        return is_valid_row_index and is_valid_col_index

    def __get_cell(self, coordinate: Tuple[int, int]) -> bool:
        """
        Returns cell corresponding to given coordinate

        :param coordinate: a tuple of form (row index, column index) giving
        the coordinate of a cell in the state

        :returns cell corresponding to given coordinate
        """
        row_index, col_index = coordinate
        return self.state[row_index][col_index]