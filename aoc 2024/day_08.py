import sys, collections, itertools

with open(r'input_6.txt') as file:
    content = file.read()

cells = set()
antennas_by_frequency = collections.defaultdict(set)
for r, line in enumerate(content.splitlines()):
    for c, char in enumerate(line):
        cell = r + c*1j
        cells.add(cell)
        if char != '.':
            antennas_by_frequency[char].add(cell)

antinodes = set()
for frequency, antennas in antennas_by_frequency.items():
    for a, b in itertools.combinations(antennas, 2):
        antinodes |= {2*a - b, 2*b - a} & cells

p1 = len(antinodes)
print(p1)

assert len(content.splitlines()) <= 50

antinodes = set()
for frequency, antennas in antennas_by_frequency.items():
    for a, b in itertools.combinations(antennas, 2):
        antinodes |= {b + (b-a)*i for i in range(-50, +50)} & cells

p2 = len(antinodes)
print(p2)