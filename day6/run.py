from typing import List
import numpy as np
from src.lanternfish import simulate_growth

if __name__ == '__main__':
    file_path = 'data/data.txt'

    initial_population: List[int] = [int(timer) for timer in open(file_path, 'r').readline().split(',')]

    print(
        'The answer to part one is {}'.format(
            np.sum(
                simulate_growth(
                    initial_population=initial_population,
                    days_to_simulate=80
                )
            )
        )
    )

    print(
        'The answer to part two is {}'.format(
            np.sum(
                simulate_growth(
                    initial_population=initial_population,
                    days_to_simulate=256
                )
            )
        )
    )
