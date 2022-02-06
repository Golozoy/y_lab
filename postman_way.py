#!/usr/bin/python


import itertools


POST_OFFICE: tuple = (0, 2)
STREETS_DICT = {
        'Griboedova': (2, 5),
        'Beiker': (5, 2),
        'Sadovay': (6, 6),
        'Vechnozelenay': (8, 3)
        }


def main() -> None:
    way_dict = finding_all_ways()
    find_short_way(way_dict)
    streets_name = find_short_way(way_dict)
    pretty_print(streets_name, way_dict)


def gen_len_way(street_1: tuple, street_2: tuple) -> float:
    """
    Метод получает два картежа(X, Y) и возвращяет их средне-квадратичное.
    """
    res = ((street_1[0] - street_2[0])** 2 + (street_1[1] - street_2[1])** 2)
    return res ** 0.5


def finding_all_ways() -> dict:
    """
    Метод перебирает все комбинации улиц и возвращает словарь, где ключем является
    строка улиц, а значение список с растояниями между ними.
    """
    permutations_gen = itertools.permutations(STREETS_DICT)
    way_dict = dict()

    for streets_list in permutations_gen:
        way_list = list()
        way_list.append(gen_len_way(POST_OFFICE, STREETS_DICT[streets_list[0]]))

        for index in range(len(streets_list) - 1):
            way_list.append(gen_len_way(STREETS_DICT[streets_list[index]],
                 STREETS_DICT[streets_list[index+1]]))

        way_list.append(gen_len_way(POST_OFFICE, STREETS_DICT[streets_list[-1]]))
        way_dict[' '.join(streets_list)] = way_list

    return way_dict


def find_short_way(way_dict: dict) -> str:
    """
    Метод ищет самый короткий путь в списке и возрашает строку с улицами.
    """
    tmp_key: str = ''
    tmp_sum_way: float = float('inf')
    for key, value in way_dict.items():
        if tmp_sum_way >= sum(value):
            tmp_sum_way = sum(value)
            tmp_key = key
    return tmp_key


def pretty_print(streets_name: str, way_dict: dict) -> None:
    """
    Ввыводит кротчайший путь в заданном стандарте
    """
    ways = way_dict[streets_name]
    streets: list = streets_name.split()
    print(POST_OFFICE, end=' -> ')
    for index in range(len(streets)):
        print(f'{STREETS_DICT[streets[index]]}{sum(ways[:index+1])}', end=' -> ')
    print(f"{POST_OFFICE} = {sum(ways)}")



if __name__ == '__main__':
    main()
