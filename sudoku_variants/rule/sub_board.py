from typing import List

import sys
from pathlib import Path

sys.path.append(str((Path(__file__) / "..").resolve()))
from interface import Rule

sys.path.append(str((Path(__file__) / ".." / "..").resolve()))
from sudoku_const import NUM_ROW, NUM_COL, DIGITS


class SubBoard(Rule):
    def check_move(self, board: List[List[int]], row: int, col: int, digit: int) -> bool:
        if digit not in DIGITS:
            return True

        sub_board_index = row // 3 * 3 + col // 3
        row_start = sub_board_index // 3 * 3
        row_end = row_start + 3
        col_start = sub_board_index % 3 * 3
        col_end = col_start + 3

        for i in range(row_start, row_end):
            for j in range(col_start, col_end):
                cur_digit = board[i][j]
                if (cur_digit == digit) and ((i != row) or (j != col)):
                    return False

        return True

    def remove_candidates(
        self, candidates: List[List[List[bool]]], row: int, col: int, digit: int
    ) -> List[List[List[bool]]]:
        if digit in DIGITS:
            sub_board_index = row // 3 * 3 + col // 3
            row_start = sub_board_index // 3 * 3
            row_end = row_start + 3
            col_start = sub_board_index % 3 * 3
            col_end = col_start + 3

            for i in range(row_start, row_end):
                for j in range(col_start, col_end):
                    if (i, j) != (row, col):
                        candidates[i][j][digit - 1] = False

        return candidates
