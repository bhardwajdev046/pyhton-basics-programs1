from collections import deque

row, col = map(int, input().split())

grid = []

for _ in range(row):
    grid.append(list(map(int, input().split())))

q = deque()
fresh = 0
time = 0

for i in range(row):
    for j in range(col):
        if grid[i][j] == 2:
            q.append((i, j))
        elif grid[i][j] == 1:
            fresh += 1

while q and fresh > 0:
    rotten = len(q)
    time += 1

    while rotten:
        i, j = q.popleft()

        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr = i + dx
            nc = j + dy

            if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 1:
                q.append((nr, nc))
                grid[nr][nc] = 2
                fresh -= 1

        rotten -= 1

if fresh > 0:
    print(-1)
else:
    print(time)