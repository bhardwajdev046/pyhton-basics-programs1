from collections import deque
n = int(input())
m = int(input())
edges=[]
for _ in range(m):
    temp = [int(x) for x in input().split()]
    edges.append(temp)

lst = [[] for _ in range(n+1)]
for u, v in edges:
    lst[u].append(v)
    lst[v].append(u)


def bfs(node, lst, n):
    visited=[-1]*(n+1)
    q = deque()
    q.append(node)
    visited[node]=1
    ans=[]
    while q:
        node = q.popleft()
        ans.append(node)
        for x in lst[node]:
            if visited[x]==-1:
                visited[x]=0
                q.append(x)
    return ans
print(bfs(1, lst, n))
