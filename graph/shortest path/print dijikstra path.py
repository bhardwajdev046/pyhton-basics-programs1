import heapq

V, E = map(int, input().split())

edges = []
for _ in range(E):
    u, v, w = map(int, input().split())
    edges.append([u, v, w])

src, dest = map(int, input().split())

lst = [[] for _ in range(V + 1)]

for u, v, w in edges:
    lst[u].append([v, w])
    lst[v].append([u, w])

parent = [i for i in range(V + 1)]
dis = [float('inf')] * (V + 1)

PQ = [[0, src]]
dis[src] = 0

while PQ:
    curr_d, node = heapq.heappop(PQ)

    if curr_d > dis[node]:
        continue

    for x, w in lst[node]:
        new_d = curr_d + w

        if new_d < dis[x]:
            dis[x] = new_d
            parent[x] = node
            heapq.heappush(PQ, [new_d, x])

if dis[dest] == float('inf'):
    print([-1])
else:
    path = []
    node = dest

    while parent[node] != node:
        path.append(node)
        node = parent[node]

    path.append(src)
    path.reverse()

    print(path)