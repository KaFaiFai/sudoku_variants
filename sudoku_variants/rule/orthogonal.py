from typing import List

import sys
from pathlib import Path

sys.path.append(str((Path(__file__) / "..").resolve()))
from interface import Rule

sys.path.append(str((Path(__file__) / ".." / "..").resolve()))
from helper.const import NUM_ROW, NUM_COL, DIGITS


class Orthogonal(Rule):
    def check_move(
        self, board: List[List[int]], row: int, col: int, digit: int
    ) -> bool:
        if digit not in DIGITS:
            return True

        for col_index in range(NUM_COL):
            cur_digit = board[row][col_index]
            if (cur_digit == digit) and (col_index != col):
                return False

        for row_index in range(NUM_ROW):
            cur_digit = board[row_index][col]
            if (cur_digit == digit) and (row_index != row):
                return False

        return True

    def remove_candidates(
        self, candidates: List[List[List[bool]]], row: int, col: int, digit: int
    ) -> List[List[List[bool]]]:
        if digit in DIGITS:
            for col_index in range(NUM_COL):
                candidates[row][col_index][digit - 1] = False

            for row_index in range(NUM_ROW):
                candidates[row_index][col][digit - 1] = False

            candidates[row][col] = [False for _ in range(len(DIGITS))]

        return candidates
