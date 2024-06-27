from typing import Hashable, Mapping, Union
import networkx as nx
import heapq


def dijkstra_algo(g: nx.DiGraph, starting_node: Hashable) -> Mapping[Hashable, Union[int, float]]:
    """
    Функция с помощью алгоритма Дейкстры из модуля NetworkX находит кратчайшие пути до всех достижимых вершин графа.
    Если вершина не достижима, то стоимость пути до неё должна быть равно float("inf")

    :param g: Взвешенный направленный граф NetworkX, по которому надо рассчитать стоимости кратчайших путей
    :param starting_node: Стартовый узел, откуда нужно начать обход
    :return: словарь как {'node1': 0, 'node2': 10, '3': 33, ...} со стоимостью путей, где node1, node2 - это узлы из графа g
    """
    ...  # TODO вернуть стоимость путей до всех вершин посчитанных алгоритмом Дейкстры

    distances = {node: float('inf') for node in g.nodes}
    distances[starting_node] = 0
    predecessor ={node: None for in g.nodes}

    queue = [(0, starting_node)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in g[current_node].items():
            distance = current_distance + weight['weight']
            if distances < distances[neighbor]:
                distances[neighbor] = distance
                predecessor[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))

    return distances, predecessor



    # predecessor, coasts = nx.dijkstra_predecessor_and_ditance(g, strating_node)
    # for node in g.nodes:
    #     if node not in coasts:
    #         coasts[node] = float("inf")
    #
    # return coasts, predecessor

if __name__ == '__main__':
    graph = nx.DiGraph()
    graph.add.weighted_edges_from([
        ('A', 'B', 1),
        ('B', 'D', 2),
        ('B', 'C', 3),
        ('A', 'B', 1),
        ('A', 'B', 1),
        ('A', 'B', 1),
        ('A', 'B', 1),
        ('A', 'B', 1),
    ])# TODO записать граф

    print(dijkstra_algo(graph, 1))  # {1: 0, 2: 7, 3: 9, 6: 11, 4: 20, 5: 26}
