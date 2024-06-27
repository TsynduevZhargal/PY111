from typing import Hashable, List
from collections import deque
import matplotlib.pyplot as plt
import networkx as nx


def bfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Функция выполняет обход в ширину и возвращает список узлов в порядке посещения.
    В данной задаче порядок обхода графа левосторонний или правосторонний не важен,
    главное соблюсти порядок обхода в ширину.

    :param g: Граф NetworkX, по которому нужно совершить обход
    :param start_node: Стартовый узел, откуда нужно начать обход
    :return: Список узлов в порядке посещения.
    """
    # TODO реализовать обход в ширину
    visited = {node: False for node in g.nodes}
    d = deque()
    path = []

    d.append(start_node)
    visited[start_node] = True

    while d:
        current_node = d.popleft()
        path.append(current_node)

        for neighbor in current_node.neighbor():
            if not visited[neighbor]:
                d.append(neighbor)
                visited[neighbor] = True

    return path

if __name__ == '__main__':
    # TODO записать граф с помощью модуля networkx и прверить обход в ширину
    graph = nx.Graph()
    graph.add_nodes_from('ABCDEFGHIJ')
    graph.add_edges_from([('A', 'B'),
                          ('A', 'F'),
                          ('B', 'G'),
                          ('G', 'C'),
                          ('G', 'H'),
                          ('G', 'I'),
                          ('G', 'C'),
                          ('C', 'H'),
                          ('H', 'I'),
                          ('H', 'J'),
                          ('H', 'E'),
                          ('H', 'D'),
                          ('E', 'D')])
    print(bfs(graph, 'A'))
    # nx.draw(graph)
    #
    # plt.show()