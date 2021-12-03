if __name__ == '__main__':
    file_path = 'data/data.txt'
    counter = [0 for _ in range(12)]
    measures_length = 0

    with open(file_path, 'r') as file:
        for measure in file:
            measures_length += 1
            for index in range(len(measure.strip('\n'))):
                counter[index] += 1 if measure[index] == '1' else 0

    gamma_rate = ''.join(
        list(
            map(
                lambda proportion: '1' if proportion >= 0.5 else '0',
                map(
                    lambda count: count/measures_length,
                    counter
                )
            )
        )
    )

    epsilon_rate = ''.join(
        list(
            map(
                lambda x: '1' if x == '0' else '0',
                gamma_rate
            )
        )
    )

    print(
        'The answer to part one is {}'.format(
            int(gamma_rate, 2) * int(epsilon_rate, 2)
        )
    )

    with open(file_path, 'r') as file:
        measurements = [measure.strip('\n') for measure in file]
        oxygen_candidates = measurements
        co2_candidates = measurements

        for index in range(len(gamma_rate)):
            oxygen_counter = 0
            co2_counter = 0

            for element in oxygen_candidates:
                oxygen_counter += 1 if element[index] == '1' else 0

            for element in co2_candidates:
                co2_counter += 1 if element[index] == '1' else 0

            if len(oxygen_candidates) > 1:
                most_popular_in_oxygen = '1' if oxygen_counter/len(oxygen_candidates) >= 0.5 else '0'
                oxygen_candidates = list(
                    filter(
                        lambda candidate: candidate[index] == most_popular_in_oxygen,
                        oxygen_candidates
                    )
                )

            if len(co2_candidates) > 1:
                less_popular_in_co2 = '1' if co2_counter/len(co2_candidates) < 0.5 else '0'
                co2_candidates = list(
                    filter(
                        lambda candidate: candidate[index] == less_popular_in_co2,
                        co2_candidates
                    )
                )

    print(
        'The answer to part two is {}'.format(
            int(co2_candidates.pop(), 2) * int(oxygen_candidates.pop(), 2)
        )
    )