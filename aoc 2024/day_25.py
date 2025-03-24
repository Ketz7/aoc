import itertools as itt

with open("input.txt") as in_f:
    DD = in_f.read().strip()
ans = 0

ks = set()
for block in DD.split("\n\n"):
    g = set()
    for y, line in enumerate(block.splitlines()):
        for x, c in enumerate(line):
            if c == "#":
                g.add(complex(x, y))
    ks.add(frozenset(g))

for a, b in itt.combinations(ks, 2):
    if not a & b:
        ans += 1
print(ans)