from typing import List, Set
from functools import reduce


def _check_victory_on_board(board: List[List[int]], drawn_numbers: Set[int]) -> bool:
    for row in map(set, board):
        if row.issubset(drawn_numbers):
            return True

    for column in map(set, zip(*board)):
        if column.issubset(drawn_numbers):
            return True

    return False


class BingoBoard:
    def __init__(self, file_path: str, board_size: int = 5):
        self.board_size: int = board_size
        self._current_number_index: int = 0

        with open(file_path, 'r') as file:
            self.random_order: List[int] = list(
                map(
                    int,
                    file.readline().split(',')
                )
            )

            rows: List[List[int]] = [
                list(map(int, line.strip('\n').split()))
                for line
                in file.readlines()
                if line != '\n'
            ]

            self.random_boards: List[List[List[int]]] = [
                rows[index:index + board_size]
                for index
                in range(0, len(rows) - board_size + 1, board_size)
            ]

    @property
    def unmarked_numbers(self) -> List[int]:
        drawn_numbers = set(self.random_order[:self._current_number_index + 1])

        return [
            number
            for board in self.random_boards
            if _check_victory_on_board(board, drawn_numbers)
            for row in board
            for number in row
            if number not in drawn_numbers
        ]

    def check_victory(self) -> bool:
        drawn_numbers = set(self.random_order[:self._current_number_index + 1])

        return reduce(
            lambda x, y: x or _check_victory_on_board(y, drawn_numbers),
            self.random_boards,
            False
        )

    def run_game(self):
        for _ in self.random_order:
            if self.check_victory():
                return self
            self._current_number_index += 1

        return self

    @property
    def score(self) -> int:
        return sum(self.unmarked_numbers) * self.random_order[self._current_number_index]
