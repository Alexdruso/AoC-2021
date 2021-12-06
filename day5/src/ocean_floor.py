from collections import Counter, defaultdict
from typing import DefaultDict, Tuple


class OceanFloor:
    def __init__(self, file_path: str):
        self.map: Counter[Tuple[int, int]] = Counter(
            [
                (x, y)
                for span in [
                [
                    list(map(int, line[0].split(','))),
                    list(map(int, line[1].split(',')))
                ]
                for line
                in [
                    line.strip('\n').split(' -> ')
                    for line
                    in open(file_path, 'r').readlines()
                ]
            ]
                for x in range(span[0][0], span[0][1] + 1)
                for y in range(span[1][0], span[1][1] + 1)
                if x == y
            ]
        )

        print(
            [
                (x, y)
                for span in [
                [
                    list(map(int, line[0].split(','))),
                    list(map(int, line[1].split(',')))
                ]
                for line
                in [
                    line.strip('\n').split(' -> ')
                    for line
                    in open(file_path, 'r').readlines()
                ]
            ]
                for x in range(span[0][0], span[0][1] + 1)
                for y in range(span[1][0], span[1][1] + 1)
                if x == y
            ]
        )

    @property
    def number_overlapping(self) -> int:
        print(self.map.items())

        return sum(
            map(
                lambda item: item[1] > 1,
                self.map.items()
            )
        )
