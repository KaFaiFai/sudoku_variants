from typing import List

import sys
from pathlib import Path

sys.path.append(str((Path(__file__) / "..").resolve()))
from interface import Rule

sys.path.append(str((Path(__file__) / ".." / "..").resolve()))
from sudoku_const import NUM_ROW, NUM_COL, DIGITS


class Knight(Rule):
    knight_moves = (
        (-2, 1),
        (-1, 2),
        (1, 2),
        (2, 1),
        (2, -1),
        (1, -2),
        (-1, -2),
        (-2, -1),
    )

    def check_move(self, board: List[List[int]], row: int, col: int, digit: int) -> bool:
        if digit not in DIGITS:
            return True

        for m in self.knight_moves:
            try:
                knightDigit = board[row + m[0]][col + m[1]]
                if digit == knightDigit:
                    return False
            except IndexError:
                pass

        return True
