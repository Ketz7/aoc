import numpy as np
import re

aoc = np.array([[*map(int, re.findall(r'-?\d+', line))] for line in open('input_6.txt').read().splitlines()])
W,H,M = 101,103,float('inf')

for r in range(1, W*H):
    aoc[:, :2] = (aoc[:, :2] + aoc[:, 2:]) % [W,H]
    p = np.prod([
        np.sum((aoc[:,0] < W//2) & (aoc[:,1] < H//2)),
        np.sum((aoc[:,0] > W//2) & (aoc[:,1] < H//2)),
        np.sum((aoc[:,0] < W//2) & (aoc[:,1] > H//2)),
        np.sum((aoc[:,0] > W//2) & (aoc[:,1] > H//2))])
    if r == 100: part1 = p
    if p < M: M, part2 = p, r

print(f'part 1: {part1} part 2: {part2}')

z = float('inf')

print(z)