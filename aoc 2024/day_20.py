import networkx as nx
import numpy as np
from aoc_helper import extract_maze

GRID, MAZE = extract_maze(open('input.txt').read())
print(GRID)
print("*" * 20)
print(MAZE)
S = tuple(np.argwhere(GRID == "S").reshape(-1).tolist())
E = tuple(np.argwhere(GRID == "E").reshape(-1).tolist())
TARGET_LENGTH = nx.shortest_path_length(MAZE, S, E) - 100

def ncheats(cheat_duration):
    cost_from_start = nx.shortest_path_length(MAZE, S)
    cost_from_end = nx.shortest_path_length(MAZE, E)
    return sum(
        start_cost + manhattan + end_cost <= TARGET_LENGTH
        for (y1, x1), start_cost in cost_from_start.items()
        for (y2, x2), end_cost in cost_from_end.items()
        if (manhattan := abs(y2 - y1) + abs(x2 - x1)) <= cheat_duration
    )

def part_one():
    return ncheats(2)

def part_two():
    return ncheats(20)

print(part_two())