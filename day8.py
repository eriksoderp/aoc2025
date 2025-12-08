from networkx import Graph, connected_components, is_connected
from math import prod
junctions = [tuple(map(int, line.strip().split(','))) for line in open('input8.txt').readlines()]

dist = lambda p, q: sum((a - b) ** 2 for a, b in zip(p, q)) ** 0.5
dists = []
for i, p in enumerate(junctions):
    for q in junctions[i+1:]:
        dists.append((p, q, dist(p, q)))
dists.sort(key=lambda x: x[2])

G = Graph()
G.add_nodes_from(junctions)
i = 0
while not is_connected(G):
    if i == 1000:
        component_lengths = [len(c) for c in connected_components(G)]
        component_lengths.sort()
        print("Part 1:", prod(component_lengths[-3:]))

    p, q, _ = dists[i]
    G.add_edge(p, q)
    i += 1

p, q, _ = dists[i-1]
print("Part 2:", p[0]*q[0])
