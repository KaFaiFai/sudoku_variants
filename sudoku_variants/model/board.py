from typing import List, TypeVar, Generic, Tuple

import sys
from pathlib import Path

sys.path.append(str((Path(__file__) / "..").resolve()))
from coord import Coord

T = TypeVar("T")
W = TypeVar("W")


class Board(Generic[T]):
    obj_copied = 0

    def __init__(self, board: List[List[T]]) -> None:
        are_rows_same_length = _are_all_elements_same([len(row) for row in board])
        if not are_rows_same_length:
            raise TypeError("Board must be a non_empty 2D-grid")
        self.board = board

    @property
    def num_row(self):
        return len(self.board)

    @property
    def num_col(self):
        return len(self.board[0])

    def get_or_none(self, coord: Coord):
        """
        Try to get the element at coord.
        Return None if out of bound
        """
        if (0 <= coord.row < self.num_row) and (0 <= coord.col < self.num_col):
            return self.board[coord.row][coord.col]
        return None

    def set_or_pass(self, coord: Coord, element: T):
        """
        Try to set the element at coord to be element.
        Do nothing if out of bound
        """
        if (0 <= coord.row < self.num_row) and (0 <= coord.col < self.num_col):
            self.board[coord.row][coord.col] = element

    # def enumerate(self) -> List[Tuple[Coord, T]]:
    #     return [(Coord(i, j), e) for i, row in enumerate(self.board) for j, e in enumerate(row)]

    @staticmethod
    def new(num_row: int, num_col: int, element: W) -> "Board[W]":
        # can't use * num_row; otherwise all rows will have the same list reference
        board = [[element] * num_col for _ in range(num_row)]
        return Board(board)

    def copy(self) -> "Board[T]":
        self.__class__.obj_copied += 1
        return Board([[e for e in row] for row in self.board])

    def __repr__(self):
        kv_list = [
            f"{k}={v}" for k, v in self.__dict__.items() if not k.startswith("_")
        ]
        repr = f"{self.__class__.__name__}({', '.join(kv_list)})"
        return repr


def _are_all_elements_same(lst: List) -> bool:
    if len(lst) == 0:
        # Empty list is considered false
        return False

    first_element = lst[0]

    for element in lst[1:]:
        if element != first_element:
            return False

    return True


def shape_of_board(board: List[List]) -> Tuple[int, int]:
    return len(board), len(board[0])


def copy_board(board: List[List[T]]) -> List[List[T]]:
    return [[d for d in row] for row in board]
