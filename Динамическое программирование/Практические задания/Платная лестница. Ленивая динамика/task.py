from typing import Union, Sequence
from functools import lru_cache


def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """
    Рассчитайте минимальную стоимость подъема на верхнюю ступень,
    если мальчик умеет наступать на следующую ступень и перешагивать через одну.

    :param stairway: список целых чисел, где каждое целое число является стоимостью конкретной ступени
    :return: минимальная стоимость подъема на верхнюю ступень
    """
    ...  # TODO реализовать ленивую динамику

    def rec_find(stairway, n):
        if n == 0 or n == 1:
            return stairway[n]
        #
        # if n == 0:
        #     return stairway[0]
        #
        # if n == 1:
        #     return stairway[1]

        return stairway[n] + min(rec_find(stairway, n-1),
                                 rec_find(stairway, n - 2))

    return rec_find(stairway, len(stairway) - 1)



if __name__ == '__main__':
    print(stairway_path((1, 3, 1, 5)))  # 7
