import sys
from pathlib import Path

sys.path.append(str((Path(__file__) / "..").resolve()))
# from board import Board
# from coord import Coord
# from move import Move
from board import copy_board, shape_of_board
