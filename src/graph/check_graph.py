from pathlib import Path
import pickle

PROJECT_ROOT = Path(__file__).resolve().parents[2]

GRAPH_FILE = PROJECT_ROOT / "data" / "graph" / "road_graph.pkl"

with open(GRAPH_FILE, "rb") as f:
    graph = pickle.load(f)

print("=" * 50)
print("ROAD GRAPH")
print("=" * 50)

print(f"Nodes : {graph.number_of_nodes():,}")
print(f"Edges : {graph.number_of_edges():,}")

print()

print("Sample Nodes:")

for node in list(graph.nodes())[:10]:
    print(node)
