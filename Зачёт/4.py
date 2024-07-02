# Навигатор на сетке.
# Дана плоская квадратная двумерная сетка (массив), на которой определена стоимость захода в каждую ячейку (все стоимости положительные).
# Необходимо найти путь минимальной стоимости из заданной ячейки в заданную ячейку и вывести этот путь.



import pprint
from typing import List


def rocket_coasts(table: List[List[int]]) -> List[List[int]]:
    x = len(table)
    y = len(table[0])

    table_cost = [[0] * y for i in range(x)]
    table_cost[0][0] = table[0][0]

    for idx in range(1, y):
        table_cost[0][idx] = table_cost[0][idx - 1] + table[0][idx]

    for idx in range(1, x):
        table_cost[idx][0] = table_cost[idx - 1][0] + table[idx][0]

    pprint.pprint(table_cost, width=30)

    for n in range(1, x):
        for m in range(1, y):
            table_cost[n][m] = min(table_cost[n - 1][m], table_cost[n][m - 1]) + table[n][m]
            print("Итерация")
            pprint.pprint(table_cost, width=30)

    print()
    pprint.pprint(table_cost, width=30)

    return table_cost


if __name__ == '__main__':
    coasts_ceil = [
        [1, 2, 3],
        [3, 2, 1],
        [1, 2, 3]
    ]
    total_coasts = rocket_coasts(coasts_ceil)
    print(total_coasts[-1][-1])  # 9
