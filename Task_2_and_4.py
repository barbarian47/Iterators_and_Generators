def flat_generator(input_list):
    lst = []
    for element in input_list:
        if isinstance(element, list):
            lst.extend(flat_generator(element))
        else:
            lst.append(element)

    return lst


if __name__ == "__main__":
    nested_list = [
        ['a', 'b', 'c', [9, 10, [True, 11]]],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
    ]


    for item in flat_generator(nested_list):
        print(item)