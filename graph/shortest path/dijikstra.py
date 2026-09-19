import heapq
def dijkstra(V, edges, src):
    lst = [[] for _ in range(V)]
    for u, v, w in edges:
        lst[u].append([v, w])
        lst[v].append([u, w])

    dist = [float('inf')] * V
    dist[src] = 0
    p_heap = [(0, src)]
    while p_heap:
        curr_d, node = heapq.heappop(p_heap)
        if curr_d > dist[node]:
            continue
        for x, d in lst[node]:
            new_d = curr_d + d
            if new_d < dist[x]:
                dist[x] = new_d
                heapq.heappush(p_heap, (new_d, x))
    return dist


#  -------------------Implement using set----------------------

    # my_set = {(0, src)}
    # while my_set:
    #     curr_d, node = min(my_set)
    #     my_set.discard((curr_d, node))
    #     for x, d in lst[node]:
    #         new_d = curr_d + d
    #         if new_d < dist[x]:
    #             if dist[x] != float('inf'):
    #                 my_set.discard((dist[x], x))
    #             dist[x] = new_d
    #             my_set.add((new_d, x))

    # return dist

V = int(input())
E = int(input())

edges = []
for _ in range(E):
    u, v, w = map(int, input().split())
    edges.append([u, v, w])
src = int(input())
answer = dijkstra(V, edges, src)
print(answer)