from itertools import combinations

import os
import sys
from pathlib import Path

sys.path.append(str((Path(__file__) / ".." / "..").resolve()))
from sudoku_variants import Sudoku, SudokuAI, SudokuConst
from sudoku_variants.rule import Orthogonal, SubBoard, Knight, King, Consecutive
from sudoku_variants.func import rules as R
from sudoku_variants.helper.profile import profile


def standard_rules():
    return [Orthogonal(), SubBoard()]


def variant_rules():
    return [Knight(), King(), Consecutive()]


# @profile(1)
def run():
    # sudoku = SudokuAI.generate([Orthogonal(), SubBoard(), Knight()], max_erased=1)
    # print(sudoku)
    # if sudoku is not None:
    #     print(sudoku.board)

    board = [
        [6, 8, 2, 3, 5, 4, 9, 1, 7],
        [5, 9, 3, 7, 1, 2, 8, 6, 4],
        [4, 1, 7, 6, 9, 8, 5, 3, 2],
        [2, 7, 8, 4, 6, 9, 1, 5, 3],
        [9, 5, 4, 1, 3, 7, 2, 8, 6],
        [1, 3, 6, 2, 8, 5, 7, 4, 9],
        [3, 6, 9, 8, 2, 1, 4, 7, 5],
        [8, 4, 5, 9, 7, 6, 3, 2, 1],
        [7, 2, 1, 5, 4, 3, 6, 9, 8],
    ]
    check = Knight().check_move(board, 0, 0, 6)
    print(check)


if __name__ == "__main__":
    run()
