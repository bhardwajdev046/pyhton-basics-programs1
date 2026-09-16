def dfs(node, lst, vis, pathvis):
    vis[node] = 1
    pathvis[node] = 1

    for x in lst[node]:
        if vis[x] == 0:
            ans = dfs(x, lst, vis, pathvis)
            if ans:
                return True

        elif pathvis[x] != 0:
            return True

    pathvis[node] = 0
    return False


V = int(input())
E = int(input())

lst = [[] for _ in range(V)]

for _ in range(E):
    u, v = map(int, input().split())
    lst[u].append(v)

vis = [0] * V
pathvis = [0] * V

flag = False

for i in range(V):
    if vis[i] == 0:
        if dfs(i, lst, vis, pathvis):
            flag = True
            break

print(flag)