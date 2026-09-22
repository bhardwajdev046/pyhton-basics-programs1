row, col = map(int, input().split())

grid = []
for _ in range(row):
    grid.append(list(input().strip()))

def dfs(i, j, visited):
    # visited[i][j] = 1
    # for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
    #     nr = i + dx
    #     nc = j + dy
    #     if (nr >= 0 and nr < row and nc >= 0 and nc < col
    #         and visited[nr][nc] == 0
    #         and grid[nr][nc] == '1'):
    #         dfs(nr, nc, visited)

# ----------------------OR-----------------------

    if i<0 or i>=row or j<0 or j>=col:
        return
    
    if visited[i][j]==1:
        return
    if grid[i][j]=='0':
        return
    visited[i][j]=1
    dfs(i+1,j,visited)
    dfs(i-1,j,visited)
    dfs(i,j+1,visited)
    dfs(i,j+1,visited)

visited = [[0] * col for _ in range(row)]
count = 0
for i in range(row):
    for j in range(col):
        if grid[i][j] == '1' and visited[i][j] == 0:
            count += 1
            dfs(i, j, visited)

print(count)


# from collections import deque
# row, col = map(int, input().split())
# grid = []
# for _ in range(row):
#     grid.append(list(input().strip()))
# visited = [[0] * col for _ in range(row)]

# def bfs(i, j):
#     q = deque()
#     q.append((i, j))
#     visited[i][j] = 1
#     while q:
#         r, c = q.popleft()

#         for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
#             nr = r + dx
#             nc = c + dy
#             if (nr >= 0 and nr < row and nc >= 0 and nc < col
#                 and visited[nr][nc] == 0
#                 and grid[nr][nc] == '1'):
#                 visited[nr][nc] = 1
#                 q.append((nr, nc))
# count = 0
# for i in range(row):
#     for j in range(col):
#         if grid[i][j] == '1' and visited[i][j] == 0:
#             count += 1
#             bfs(i, j)
# print(count)