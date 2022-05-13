import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())

g = [[] for i in range(n + 1)]

dis = [INF] * (n + 1)

for _ in range(m):
    gi, gj, gw = map(int, input().split())
    g[gi].append((gj,gw))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dis[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dis[now] < dist:
            continue
        for i in g[now]:
            cost = dist + i[1]
            if cost < dis[i[0]]:
                dis[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, n+1):
    if dis[i] == INF:
        print("INF")
    else:
        print(dis[i])