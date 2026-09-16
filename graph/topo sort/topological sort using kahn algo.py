from collections import deque

V = int(input())
E = int(input())

lst = [[] for _ in range(V)]
indegree = [0] * V

for _ in range(E):
    u, v = map(int, input().split())
    lst[u].append(v)
    indegree[v] += 1

q = deque()
res = []

for i in range(V):
    if indegree[i] == 0:
        q.append(i)

while q:
    node = q.popleft()
    res.append(node)

    for x in lst[node]:
        indegree[x] -= 1

        if indegree[x] == 0:
            q.append(x)

print(res)