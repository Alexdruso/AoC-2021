from src.ocean_floor import OceanFloor

if __name__ == '__main__':
    file_path = 'data/data.txt'

    ocean_floor = OceanFloor(file_path=file_path)

    print(
        'The answer to part one is {}'.format(
            ocean_floor.number_overlapping
        )
    )
