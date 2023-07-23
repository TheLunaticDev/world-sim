import utility


def main():
    test_cases = [
        '#282a36',
        '#44475a',
        '#f8f8f2',
        '#6272a4',
        '#8be9fd',
        '#50fa7b',
        '#ffb86c',
        '#ff79c6',
        '#bd93f9',
        '#ff5555',
        '#f1fa8c',
        'What are you looking at?',
        'f1fa8c',
        '',
    ]
    expected_results = [
        (40, 42, 54),
        (68, 71, 90),
        (248, 248, 242),
        (98, 114, 164),
        (139, 233, 253),
        (80, 250, 123),
        (255, 184, 108),
        (255, 121, 198),
        (189, 147, 249),
        (255, 85, 85),
        (241, 250, 140),
        None,
        None,
        None
    ]

    test_pass = 0
    test_failed = []
    for i in range(len(test_cases)):
        if utility.hex_to_rgb(test_cases[i]) == expected_results[i]:
            test_pass += 1
        else:
            test_failed.append(i)

        print('For test case ' + test_cases[i] + ' expected output ' + str(expected_results[i]) + '. Got ' + str(utility.hex_to_rgb(test_cases[i])))

    print(str(test_pass) + ' / ' + str(len(test_cases)))


if __name__ == '__main__':
    main()
