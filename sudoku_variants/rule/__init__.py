import sys
from pathlib import Path

sys.path.append(str((Path(__file__) / "..").resolve()))
from interface import Rule, RuleWithData
from rules import check_move, populate_initial_data, extract_data_from_board, to_name
from orthogonal import Orthogonal
from sub_board import SubBoard
from knight import Knight
from king import King
