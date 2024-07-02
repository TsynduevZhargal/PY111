# 3.	Назовем связным такой граф, в котором есть путь от любой вершины к любой другой вершине.
# Дан граф, состоящий из 2+ связных подграфов, которые не связаны между собой.
# Задача: посчитать число компонент связности графа, т.е. количество таких подграфов.
# В графе на картинке – три подграфа, т.е. число компонент связности = 3.



from typing import Hashable, List
from collections import deque
import matplotlib.pyplot as plt

import networkx as nx


def dfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    visited = {node: False for node in g.nodes}
    path = []

    def rec_dfs(current_node):
        visited[current_node] = True
        path.append(current_node)

        for neighbor in g.neighbor(current_node):
            if not visited[neighbor]:
                rec_dfs(neighbor)

    rec_dfs(start_node)

    return path

if __name__ == '__main__':
    graph = nx.Graph()
    graph.add_nodes_from('ABCDEFG')
    graph.add_edges_from([('A', 'B'),
                          ('B', 'C'),
                          ('C', 'D'),
                          ('G', 'F')])

    print(dfs(graph, 'A'))
