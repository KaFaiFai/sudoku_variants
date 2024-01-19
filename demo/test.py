import sys
from pathlib import Path

sys.path.append(str((Path(__file__) / ".." / "..").resolve()))
from sudoku_variants import Sudoku, SudokuAI, SudokuConst
from sudoku_variants.rule import Orthogonal, SubBoard, Knight, King, Consecutive, Jigsaw
from sudoku_variants.func import rules as R


def standard_rules():
    return [Orthogonal(), SubBoard()]


def variant_rules():
    return [Knight(), King(), Consecutive(), Jigsaw()]


def run():
    jigsaw = Jigsaw()
    print(jigsaw.data)
    sudoku = SudokuAI.generate([Orthogonal(), SubBoard(), jigsaw], max_erased=10)
    print(sudoku)
    print(jigsaw.data)


if __name__ == "__main__":
    run()
