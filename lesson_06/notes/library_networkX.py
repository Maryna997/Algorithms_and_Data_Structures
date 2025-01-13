import networkx as nx

G = nx.Graph()
G.add_node("A")
G.add_nodes_from(["B", "C", "D"])
G.add_edge("A", "B")
G.add_edges_from([("A", "C"), ("B", "C"), ("B", "D")])
print(G.nodes())  # ['A', 'B', 'C', 'D']
print(G.edges())  # [('A', 'B'), ('A', 'C'), ('B', 'C'), ('B', 'D')]
print(list(G.neighbors("A")))  # ['B', 'C']
G.remove_node("A")
G.remove_nodes_from(["B", "C"])
G.remove_edge("A", "B")
G.remove_edges_from([("A", "C"), ("B", "D")])



DG = nx.DiGraph()
DG.add_edge("A", "B")
DG.add_edge("B", "A")





G = nx.Graph()
G.add_edges_from([("A", "B"), ("B", "C")])
DG = nx.DiGraph(G)




DG = nx.DiGraph()
DG.add_edges_from([("A", "B"), ("B", "C")])
G = nx.Graph(DG)



G.add_node(1)
G.add_node("A")
G.add_node((2, 3))
G.add_edge(1, "A", weight=2.5, label="connection")
G.nodes[1]["color"] = "red"
G.edges[1, "A"]["label"] = "bridge"


neighbors_of_A = G["A"] # {'B': {}, 'C': {}}
edge_info = G["A"]["B"]  # {}
edge_weight = G["A"]["B"]["weight"]



G.graph["name"] = "My Graph"
G.nodes["A"]["color"] = "blue"
G["A"]["B"]["weight"] = 5

G.add_node("A", color="red")
G.add_edge("A", "B", weight=4)





import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_node("A")
G.add_nodes_from(["B", "C", "D"])

G.add_edge("A", "B")
G.add_edges_from([("A", "C"), ("B", "C"), ("B", "D")])

num_nodes = G.number_of_nodes()  # 4
num_edges = G.number_of_edges()  # 4
is_connected = nx.is_connected(G)  # True

degree_centrality = nx.degree_centrality(G)  # {'A': 0.6666666666666666, 'B': 1.0, 'C': 0.6666666666666666, 'D': 0.3333333333333333}
closeness_centrality = nx.closeness_centrality(G)  # {'A': 0.75, 'B': 1.0, 'C': 0.75, 'D': 0.6}
betweenness_centrality = nx.betweenness_centrality(G)  # {'A': 0.0, 'B': 0.6666666666666666, 'C': 0.0, 'D': 0.0}

path = nx.shortest_path(G, source="A", target="D")  # ['A', 'B', 'D']
avg_path_length = nx.average_shortest_path_length(G)  # 1.3333333333333333





import matplotlib.pyplot as plt
G = nx.complete_graph(8)
nx.draw(G, with_labels=True)
plt.show()

networkx.draw(G, pos=None, ax=None, **kwds)



import matplotlib.pyplot as plt
G = nx.complete_graph(4)
options = {
    "node_color": "yellow",
    "edge_color": "lightblue",
    "node_size": 500,
    "width": 3,
    "with_labels": True
}
nx.draw(G, **options)
plt.show()




import networkx as nx
import matplotlib.pyplot as plt

G = nx.complete_graph(8)
pos = nx.circular_layout(G)
nx.draw(G, pos, with_labels=True)
plt.title("Circular Layout")
plt.show()





import networkx as nx
import matplotlib.pyplot as plt

G = nx.complete_graph(8)
pos = nx.random_layout(G)
nx.draw(G, pos, with_labels=True)
plt.title("Random Layout")
plt.show()




import networkx as nx
import matplotlib.pyplot as plt

G = nx.complete_graph(8)
pos = [[0, 1, 2], [3, 4], [5, 6, 7]]  # Вказує камери для розташування вершин
pos = nx.shell_layout(G, pos)
nx.draw(G, pos, with_labels=True)
plt.title("Shell Layout")
plt.show()






import networkx as nx
import matplotlib.pyplot as plt

# Створення орієнтованого графа
G = nx.DiGraph()

# Додавання ребер
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 3), (4, 1)])

# Малювання графа
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, arrows=True)

plt.show()







import networkx as nx

# Створення графа
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

G = nx.Graph(graph)

# DFS
dfs_tree = nx.dfs_tree(G, source='A')
print(list(dfs_tree.edges()))  # виведе ребра DFS-дерева з коренем у вузлі A

# BFS
bfs_tree = nx.bfs_tree(G, source='A')
print(list(bfs_tree.edges()))  # виведе ребра BFS-дерева з коренем у вузлі A
