import networkx as nx
import matplotlib.pyplot as plt


# definition of a directed Graph G
G = nx.MultiDiGraph()


# Adding nodes to the created graph
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_node(5)

# Adding edges
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(1, 4)
G.add_edge(4, 1)
G.add_edge(5, 1)
G.add_edge(5, 4)


# Create an randon tree with n nodes
RT = nx.generators.trees.random_tree(4)

# Drawing the graph
plt.subplot(121)
nx.draw(G)
plt.subplot(122)
nx.draw(RT)

plt.show()