import random

from typing import List, Tuple, Optional
import sys
from pathlib import Path

sys.path.append(str((Path(__file__) / "..").resolve()))
from interface import Rule, RuleWithData

sys.path.append(str((Path(__file__) / ".." / "..").resolve()))
from sudoku_const import NUM_ROW, NUM_COL, DIGITS

ConsecutiveDataType = List[Tuple[Tuple[int, int], Tuple[int, int]]]


class Consecutive(Rule, RuleWithData):
    offsets = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1),
    ]

    def __init__(self, data: Optional[ConsecutiveDataType] = None) -> None:
        """
        data contains a list of neighbours which is a pair of coordinates
        """
        super().__init__()
        self.data: ConsecutiveDataType
        if data is None:
            self.data = []
        else:
            self.data = data

    def check_move(self, board: List[List[int]], row: int, col: int, digit: int) -> bool:
        if digit not in DIGITS:
            return True

        cur_coord = (row, col)
        for offset in self.offsets:
            neighbour_coord = (row + offset[0], col + offset[1])
            pair1 = (cur_coord, neighbour_coord)
            pair2 = (neighbour_coord, cur_coord)

            if pair1 in self.data or pair2 in self.data:
                neighbour_digit = board[neighbour_coord[0]][neighbour_coord[1]]
                if neighbour_digit in DIGITS and abs(digit - neighbour_digit) != 1:
                    return False

        return True

    def populate_initial_data(self):
        self.data = []

    def extract_data_from_board(self, board: List[List[int]]):
        data = []
        for i in range(NUM_ROW):
            for j in range(NUM_COL):
                cur_coord = (i, j)
                cur_digit = board[i][j]

                for offset in self.offsets:
                    try:
                        neighbour_coord = (i + offset[0], j + offset[1])
                        neighbour_digit = board[neighbour_coord[0]][neighbour_coord[1]]
                        if abs(cur_digit - neighbour_digit) == 1:
                            data.append((cur_coord, neighbour_coord))
                    except IndexError:
                        pass

        size = random.randint(0, len(data))
        self.data = random.sample(data, size)
