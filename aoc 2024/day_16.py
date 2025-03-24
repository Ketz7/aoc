# import heapq

# grid = [list(line.strip()) for line in open('input.txt') ]

# rows = len(grid)
# cols = len(grid[0])

# for r in range(rows):
#     for c in range(cols):
#         if grid[r][c] == 'S':
#             sr = r
#             sc = c
#             break
#     else:
#         continue
#     break

# pq2= [(0, sr, sc, 0, 1)]
# lowest_cost = {(sr, sc, 0 , 1) : 0}
# backtrack = {}
# best_cost = float("inf")
# end_states = set()



# def p1():
#     grid = [list(line.strip()) for line in open('input.txt') ]

#     rows = len(grid)
#     cols = len(grid[0])

#     for r in range(rows):
#         for c in range(cols):
#             if grid[r][c] == 'S':
#                 sr = r
#                 sc = c
#                 break
#         else:
#             continue
#         break
#     pq= [(0, sr, sc, 0, 1)]
#     seen = {(sr, sc, 0 , 1)}

#     while pq:
#         cost, r, c, dr, dc = heapq.heappop(pq)
#         seen.add((r, c, dr, dc))
#         if grid[r][c] == 'E':
#             print(cost)
#             break
#         for new_cost, nr, nc, ndr, ndc in [(cost + 1, r + dr, c + dc, dr, dc), (cost + 1000, r, c, dc, -dr), (cost + 1000, r, c, -dc, dr)]:
#             if grid[nr][nc] == '#': continue
#             if (nr, nc, ndr, ndc) in seen: continue
#             heapq.heappush(pq, (new_cost, nr, nc, ndr, ndc))

# def p2():
#     while pq2:
#         cost, r, c, dr, dc = heapq.heappop(pq2)
        
#         if cost > lowest_cost.get((r, c, dr, dc), float("inf")) : continue
#         if grid[r][c] == 'E':
#             if cost > best_cost: break
#             best_cost = cost
#             end_states.add((r, c, dr, dc))
#         for new_cost, nr, nc, ndr, ndc in [(cost + 1, r + dr, c + dc, dr, dc), (cost + 1000, r, c, dc, -dr), (cost + 1000, r, c, -dc, dr)]:
#             if grid[nr][nc] == '#': continue
#             lowest = lowest_cost.get((r, c, dr, dc), float("inf"))
#             if new_cost > lowest: continue
#             if new_cost < lowest:
#                 backtrack[(nr, nc, ndr, ndc)] = set()
#                 lowest_cost[(nr, nc, ndr, ndc)] = new_cost
#             backtrack[(nr, nc, ndr, ndc)]. add((r, c, dr, dc))
#             heapq.heappush(pq2, (new_cost, nr, nc, ndr, ndc))
#         print(backtrack)

# print(p2())

import networkx as nx

with open("input.txt") as f:
    ls = f.read().strip().split("\n")

fourdir = (1, -1, 1j, -1j)

G = nx.DiGraph()

for i, l in enumerate(ls):
    for j, x in enumerate(l):
        if x == "#":
            continue
        z = i + 1j * j
        if x == "S":
            start = (z, 1j)
        if x == "E":
            end = z
        for dz in fourdir:
            G.add_node((z, dz))

for z, dz in G.nodes:
    if (z + dz, dz) in G.nodes:
        G.add_edge((z, dz), (z + dz, dz), weight=1)
    for rot in -1j, 1j:
        G.add_edge((z, dz), (z, dz * rot), weight=1000)

for dz in fourdir:
    G.add_edge((end, dz), "end", weight=0)

# Part 1
print(nx.shortest_path_length(G, start, "end", weight="weight"))

# Part2
print(
    len(
        {
            z
            for path in nx.all_shortest_paths(G, start, "end", weight="weight")
            for z, _ in path[:-1]
        }
    )
)