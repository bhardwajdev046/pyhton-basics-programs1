row, col = map(int, input().split())

grid = []
for _ in range(row):
    grid.append(list(input().strip()))

def dfs(i,j,visited,size,flip):
    if i<0 or i>=row or j<0 or j>=col:
        return size
    if visited[i][j]==1:
        return size
    if grid[i][j]=='0' and flip==0:
        return size
    if grid[i][j]=="0" and flip!=0:
        grid[i][j]='1'
        flip-=1
    visited[i][j]=1
    for dx,dy in((-1,0),(1,0),(0,-1),(0,1)):
        nr = dx+i
        nc = dy+j
        dfs(nr,nc,visited,size+1,flip)


visited = [[0] * col for _ in range(row)]
size=0
for i in range(row):
    for j in range(col):
        if grid[i][j] == '1' and visited[i][j] == 0:
            dfs(i,j,visited,size,1)

print(size)