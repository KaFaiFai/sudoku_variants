from dataclasses import dataclass
from typing import ClassVar


@dataclass
class Coord:
    row: int
    col: int
    obj_created: ClassVar[int] = 0

    def __post_init__(self):
        self.__class__.obj_created += 1
