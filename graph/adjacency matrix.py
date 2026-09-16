n = int(input())
m = int(input())

edges=[]

for i in range(m):
    temp = [int(x) for x in input().split()]
    edges.append(temp)

matrix = [[0]*(n+1) for _ in range(n+1)]

for i in range(len(edges)):
    u = edges[i][0]
    v = edges[i][1]

    matrix[u][v] = 1
    matrix[v][u] = 1

print(matrix)