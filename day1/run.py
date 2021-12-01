if __name__ == '__main__':

    path = 'data/data.txt'
    result = []

    with open(path, 'rb') as f:
        previous_value = None

        for line in f:
            current_value = int(line)
            result.append(previous_value is not None and current_value > previous_value)
            previous_value = current_value

    print(
        'The answer to part one is {}'.format(
            sum(result)
        )
    )

    result = [
        int(line)
        for line
        in open(path, 'rb')
    ]

    result = [
        sum(result[index:index+3])
        for index
        in range(len(result)-2)
    ]

    result = [
        result[index] > result[index-1]
        for index
        in range(1, len(result))
    ]

    result = sum(result)

    print('The answer to part two is {}'.format(result))
