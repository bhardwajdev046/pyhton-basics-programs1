# n = int(input())
# m = int(input())

# edges = []
# for i in range(m):
#     temp = [int(x) for x in input().split()]
#     edges.append(temp)

# list = [[] for _ in range(n+1)]

# for u,v in edges:
#     list[u].append(v)
#     list[v].append(u)   
# print(list)


#ADJACENCDICTIONARY/MAP 

n = int(input())
m = int(input())

edges = []
for i in range(m):
    temp = [int(x) for x in input().split()]
    edges.append(temp) 

hash ={}
for u, v in edges:
    if u not in hash:
        hash[u] = []
    if v not in hash:
        hash[v] = []
    hash[u].append(v)
    hash[v].append(u)

print(hash)