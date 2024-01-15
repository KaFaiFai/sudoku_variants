from typing import List

import sys
from pathlib import Path

sys.path.append(str((Path(__file__) / ".." / "..").resolve()))


class Rule:
    def check_move(self, board: List[List[int]], row: int, col: int, digit: int) -> bool:
        """
        Assume the given board is valid, check if the new move is valid
        """
        raise NotImplementedError("Please implement this method")

    def remove_candidates(
        self, candidates: List[List[List[bool]]], row: int, col: int, digit: int
    ) -> List[List[List[bool]]]:
        """
        Remove candidates based on the move to accelerate generation process
        """
        raise NotImplementedError("Please implement this method")

    def get_name(self) -> str:
        return type(self).__name__


class RuleWithData:
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