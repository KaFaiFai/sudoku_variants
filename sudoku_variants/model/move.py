from dataclasses import dataclass
from typing import ClassVar

import sys
from pathlib import Path

sys.path.append(str((Path(__file__) / "..").resolve()))
from coord import Coord


@dataclass
class Move:
    row: int
    col: int
    digit: int
    obj_created: ClassVar[int] = 0

    @property
    def coord(self):
        return Coord(self.row, self.col)

    @staticmethod
    def from_coord(coord: Coord, digit: int) -> "Move":
        return Move(coord.row, coord.col, digit=digit)

    def __post_init__(self):
        self.__class__.obj_created += 1
