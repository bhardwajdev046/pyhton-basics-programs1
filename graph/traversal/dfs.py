n = int(input())
m = int(input())
edges=[]
for i in range(m):
    temp = [int(x) for x in input().split()]
    edges.append(temp)

lst = [[] for _ in range(n+1)]
for u,v in edges:
    lst[u].append(v)
    lst[v].append(u)

def dfs(node, visited, lst, n, ans):
    visited[node]=1
    ans.append(node)
    for x in lst[node]:
        if visited[x]==-1:
            dfs(x,visited,lst,n,ans)
            
    return ans

visited=[-1]*(n+1)
ans=[]
print(dfs(1, visited, lst, n, ans))
