import sys
from pathlib import Path

sys.path.append(str((Path(__file__) / "..").resolve()))
from interface import Rule, RuleWithData
from orthogonal import Orthogonal
from sub_board import SubBoard
from knight import Knight
from king import King
from consecutive import Consecutive
