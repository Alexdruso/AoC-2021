from typing import List, Tuple


class Submarine:
    def __init__(self):
        self.horizontal_position: int = 0
        self.vertical_position: int = 0
        self.commands = {
            'forward': self._move_forward,
            'up': self._move_up,
            'down': self._move_down
        }

    def _move_forward(self, x: int):
        self.horizontal_position += x
        return self

    def _move_up(self, x: int):
        self.vertical_position -= x
        return self

    def _move_down(self, x: int):
        self.vertical_position += x
        return self

    def move(self, path: List[Tuple[str, int]]):
        for command, x in path:
            self.commands[command](x)
        return self


class FixedSubmarine(Submarine):
    def __init__(self):
        super().__init__()
        self.aim: int = 0

    def _move_forward(self, x: int):
        self.horizontal_position += x
        self.vertical_position += self.aim * x
        return self

    def _move_up(self, x: int):
        self.aim -= x
        return self

    def _move_down(self, x: int):
        self.aim += x
        return self
