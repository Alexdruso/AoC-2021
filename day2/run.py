from src.submarine import Submarine, FixedSubmarine

if __name__ == '__main__':
    file_path = 'data/data.txt'

    submarine = Submarine().move(
        path=[
            (line.split()[0], int(line.split()[1]))
            for line
            in open(file_path, 'r')
        ]
    )

    print(
        'The answer to part one is {}'.format(
            submarine.vertical * submarine.horizontal
        )
    )

    submarine = FixedSubmarine().move(
        path=[
            (line.split()[0], int(line.split()[1]))
            for line
            in open(file_path, 'r')
        ]
    )

    print(
        'The answer to part two is {}'.format(
            submarine.vertical * submarine.horizontal
        )
    )
