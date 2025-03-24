import re

def nums(s):
    m = re.findall(r"~?\d+", s)
    return [int(x) for x in m]

def extract_maze(raw: str, wall="#", largest_component=False):
    """Parse an ascii maze into a networkx graph. Return a tuple
    `(np.array, nx.Graph)`.
    """
    import networkx as nx
    import numpy as np

    lines = raw.splitlines()
    max_width = max(map(len, lines))
    maze = np.array([list(line + " " * (max_width - len(line))) for line in lines])

    G = nx.grid_graph(maze.shape[::-1])

    walls = np.stack(np.where(maze == wall)).T
    G.remove_nodes_from(map(tuple, walls))

    if largest_component:
        G.remove_nodes_from(
            G.nodes - max(nx.connected_components(G), key=lambda g: len(g))
        )

    return maze, G