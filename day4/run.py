from src.bingo import BingoBoard

if __name__ == '__main__':
    file_path = 'data/data.txt'

    bingo_board = BingoBoard(file_path=file_path)

    print(
        'The answer to part one is {}'.format(
            bingo_board.run_game().score
        )
    )