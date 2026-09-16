def dfs(node, lst, visited, stack):
    visited[node] = 1

    for x in lst[node]:
        if visited[x] == 0:
            dfs(x, lst, visited, stack)

    stack.append(node)


V = int(input())
E = int(input())

edges = []

for _ in range(E):
    # temp = [int(x) for x in input().split()]
    # edges.append(temp)
    #       OR
    
    u, v = map(int, input().split())
    edges.append([u, v])

lst = [[] for _ in range(V)]

for u, v in edges:
    lst[u].append(v)

visited = [0] * V
stack = []

for i in range(V):
    if visited[i] == 0:
        dfs(i, lst, visited, stack)

print(stack[::-1])