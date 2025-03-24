from collections import defaultdict

lines = [l.rstrip() for l in open('input.txt')]

connections = defaultdict(set)
nodes = set()

for l in lines: 
    # Only do a connection from the lesser to greater node
    a, b = sorted(l.split("-"))
    connections[a] |= {b}
    nodes |= {a, b}

def get_cliques(subset): 
    res = {()}
    for node in subset:
        res |= {(node,) + k for k in get_cliques(subset & connections[node])}
    return res

cliques = get_cliques(nodes)

print(len([c for c in cliques if len(c) == 3 and any(n[0] == "t" for n in c)]))
print(",".join(max(cliques, key = lambda c: len(c))))