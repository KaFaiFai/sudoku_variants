from typing import List

import sys
from pathlib import Path

sys.path.append(str((Path(__file__) / "..").resolve()))
from interface import Rule

sys.path.append(str((Path(__file__) / ".." / "..").resolve()))
from helper.const import NUM_ROW, NUM_COL, DIGITS


class King(Rule):
    king_moves = (
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    )

    def check_move(
        self, board: List[List[int]], row: int, col: int, digit: int
    ) -> bool:
        if digit not in DIGITS:
            return True

        for m in self.king_moves:
            try:
                knightDigit = board[row + m[0]][col + m[1]]
                if digit == knightDigit:
                    return False
            except:
                pass

        return True
