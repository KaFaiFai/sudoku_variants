import sys
from pathlib import Path

sys.path.append(str((Path(__file__) / "..").resolve()))
from sudoku_variants.sudoku import Sudoku
from sudoku_variants.sudokuAI import SudokuAI
