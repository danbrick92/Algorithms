# Creates seperate clusters of connected nodes that do not have crossing lines
def get_disconnected_nodes():
    nodes = {
        1: [0, 1],
        2: [5],
        3: [2, 0],
        4: [5],
        5: [3, 4, 1, 2],
        6: [6, 7],
        7: [3],
        8: [8, 6],
        9: [4],
        10: [7, 8]
    }
    edges = {
        0: (1, 3),
        1: (1, 5),
        2: (3, 5),
        3: (5, 7),
        4: (5, 9),
        5: (2, 4),
        6: (6, 8),
        7: (6, 10),
        8: (8, 10)
    }
    return { 'nodes' : nodes, 'edges' : edges}

# Creates a single cluster of connected nodes
def get_connected_nodes():
    nodes = {
        0: [0, 1],
        1: [2],
        2: [3, 4],
        3: [5, 6],
        4: [7],
        5 : []
    }
    edges = {
        0: (0, 1),
        1: (0, 2),
        2: (1, 3),
        3: (2, 3),
        4: (2, 4),
        5: (3, 4),
        6: (3, 5),
        7: (4, 5)
    }
    return {'nodes': nodes, 'edges': edges}