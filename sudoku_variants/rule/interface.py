from typing import List


class Rule:
    def description(self) -> str:
        """
        Return a brief description of the rule
        """
        raise NotImplementedError("Please implement this method")

    def check_move(self, board: List[List[int]], row: int, col: int, digit: int) -> bool:
        """
        Assume the given board is valid, check if the new move is valid
        """
        raise NotImplementedError("Please implement this method")

    def __str__(self) -> str:
        return type(self).__name__


class WithData:
    def populate_initial_data(self):
        """
        Used to reset data or initialize data before solving an empty sudoku
        """
        raise NotImplementedError("Please implement this method")

    def extract_data_from_board(self, board: List[List[int]]):
        """
        Used after solving sudoku and extract data from it
        """
        raise NotImplementedError("Please implement this method")
