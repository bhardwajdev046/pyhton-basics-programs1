# This is used to build the graph
# Each edge contains: u -> v with weight w
# Example: 0 1 5 means 0 -> 1 with weight 5

def dfs(node, stack, visited, lst):

    # Mark current node as visited
    visited[node] = 1

    # Visit all neighbours of current node
    for x in lst[node]:

        # x[0] = neighbour node
        # x[1] = edge weight
        if visited[x[0]] == 0:

            # Recursively visit the neighbour
            dfs(x[0], stack, visited, lst)

    # Add node AFTER visiting all its neighbours
    # This creates topological ordering
    stack.append(node)


# ---------------- INPUT ----------------

# Number of vertices
V = int(input())

# Number of edges
E = int(input())

# Adjacency list
# lst[u] will contain [v, weight]
lst = [[] for _ in range(V)]


# Read all edges
for _ in range(E):

    # Input format: u v w
    u, v, w = map(int, input().split())

    # Directed weighted edge: u -> v
    lst[u].append([v, w])


# ---------------- TOPOLOGICAL SORT ----------------

# visited[i] = 0 means not visited
# visited[i] = 1 means visited
visited = [0] * V

# This stack will store nodes in topological order
stack = []


# Run DFS for every node
# This is necessary because the graph may be disconnected
for i in range(V):

    if visited[i] == 0:
        dfs(i, stack, visited, lst)


# ---------------- SHORTEST PATH ----------------

# Initially, distance of every node is infinity
dis = [float('inf')] * V

# Source node is 0
# Distance from source to itself = 0
dis[0] = 0


# Process nodes according to topological order
while stack:

    # Take the last node from stack
    node = stack.pop()

    # Check all outgoing edges of this node
    for x in lst[node]:

        # x[0] = neighbour
        # x[1] = weight
        v = x[0]
        w = x[1]

        # Relaxation:
        # If going through 'node' gives a shorter distance
        if dis[node] + w < dis[v]:

            # Update shortest distance
            dis[v] = dis[node] + w


# ---------------- OUTPUT ----------------

# If a node is unreachable, its distance is still infinity
# Convert infinity to -1
for i in range(V):

    if dis[i] == float('inf'):
        dis[i] = -1


# Print final shortest distances
print(dis)