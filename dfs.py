import common.graphs as graphs
from copy import deepcopy
import math

def dfs(G, s, explored=[], f={}, current=-1):
    # Create explored list, queue
    explored.append(s)
    for item in G['nodes'][s]:
        edges = G['edges'][item]
        if edges[0] != s:
            v = edges[0]
        else:
            v = edges[1]
        if v not in explored:
            explored, f, current = dfs(G, v, explored, f, current)
    # Record topological order
    f[s] = current
    current -= 1
    return explored, f, current

def dfs_loop(G):
    # Orders graph starting at sink node and working back to base
    current = len(G['nodes'])
    explored = []
    f = {}
    nodes = list(G['nodes'].keys())
    for i in range(len(nodes)):
        v = nodes[i]
        if v not in explored:
            explored, f, current = dfs(G, v, explored, f, current)
    return f

if __name__ == "__main__":
    # Generate graph
    G = graphs.get_connected_nodes()
    # DFS basics
    explored, f, current = dfs(G, 0)
    print("Explored nodes in this order: {}".format(explored))
    # Topological Ordering
    G = graphs.get_directed_graph()
    f = dfs_loop(G)
    print("Graph ordering: {}".format(f))