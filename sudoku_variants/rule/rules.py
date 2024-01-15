from typing import List

import sys
from pathlib import Path

sys.path.append(str((Path(__file__) / "..").resolve()))
from interface import Rule, RuleWithData

# because Python doesn't have extension


def to_name(rules: List[Rule]):
    return ", ".join(r.get_name() for r in rules)


def check_move(rules: List[Rule], board: List[List[int]], row: int, col: int, digit: int) -> bool:
    return all(rule.check_move(board, row, col, digit) for rule in rules)


def populate_initial_data(rules: List[Rule]):
    for rule in rules:
        if isinstance(rule, RuleWithData):
            rule.populate_initial_data()


def extract_data_from_board(rules: List[Rule], board: List[List[int]]):
    for rule in rules:
        if isinstance(rule, RuleWithData):
            rule.extract_data_from_board(board)