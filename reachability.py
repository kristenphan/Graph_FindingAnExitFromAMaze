#Uses python3

import sys


# this function visits all nodes which are reachable from the passed in node and in depth-first order
# and makes these nodes visited
# the reachability of a particular node is determined by the passed-in adjacent node list
# the passed in 'visited' list keeps track whether a vertex v in a graph has been visited by storing boolean value: True/False
def explore(v, visited):
    visited[v] = True # mark vertex v visited right before exploring it
    for adj_node in adj[v]: # explore all reachable vertices from v
        if not visited[adj_node]:
            explore(adj_node, visited)


# this function takes in an adjacent list presenting a graph and two vertices x and y
# the function then check if x is reachable from y
# if yes, return 1
# otherwise, return 0
# BRAINSTORM
def reach(adj, x, y):
    # mark all n nodes in the graph unvisited
    n = len(adj)
    visited = [False for _ in range(n)]

    # begin exploring the graph from x
    # while exploring x, mark x as visited and other nodes reachable from x visited
    visited[x] = True
    for adj_node in adj[x]:
        if not visited[adj_node]:
            explore(adj_node, visited) # recursively explore all reachable nodes from x

    # once finished exploring, check of the other node has been visited
    # if yes, return 1 ie. reachable
    # if no, return 0 ie. not reachable
    if visited[y] == True:
        return 1
    else:
        return 0


# this program takes an input that represent a graph and checks if there is a path between a pair of vertices
# if yes, return 1. otherwise, return 0
# EXAMPLE 1:
# input given in 1-based index (and how to interpret input):
# 4 5 (explanation: n = number of vertices = 4; m = number of edges = 2)
# 1 2 (an edge connecting vertex 1 with vertex 2)
# 2 3 (an edge connecting vertex 2 with vertex 3)
# 4 3 (an edge connecting vertex 4 with vertex 3)
# 1 4 (an edge connecting vertex 1 with vertex 4)
# 2 4 (an edge connecting vertex 2 with vertex 4)
# 1 4 (explanation: check if there's a path connecting vertex 1 and 4)
# output: 1
# graph visualized in 1-based index
#     1-- 2
#     | \ |
#     4---3
# graph visualized in 0-based index
#     0-- 1
#     | \ |
#     3---2
# x = 0, y = 3
# adjacent list (adj) = [[1, 3], [0, 2], [1, 3], [0, 2]]
# vertex idx               0        1       2       3
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(reach(adj, x, y))
