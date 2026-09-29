import pickle
import networkx as nx

with open("data/graph/road_graph.pkl", "rb") as f:
    G = pickle.load(f)

print("Nodes:", G.number_of_nodes())
print("Edges:", G.number_of_edges())

components = list(nx.connected_components(G))

print("Connected Components:", len(components))

largest = max(components, key=len)

print("Largest Component:", len(largest))
