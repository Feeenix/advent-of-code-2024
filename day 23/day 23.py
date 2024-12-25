import networkx as nx
with open("day 23/input") as f:
    text = f.read().strip()
G = nx.Graph()
for line in text.split("\n"):
    a,b = line.strip().split("-")
    G.add_edge(a,b, weight=1)

triangles = [
    (u, v, w)
    for u in G.nodes
    for v in G.neighbors(u)
    for w in G.neighbors(v)
    if w in G.neighbors(u) and u < v < w  # Ensure unique triangles
]
filtered_triangles = [
    triangle for triangle in triangles if any(str(node).startswith("t") for node in triangle)
]
print( len(filtered_triangles))

