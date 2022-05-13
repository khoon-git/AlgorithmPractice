import sys

input = sys.stdin.readline
import heapq
INF = int(1e9)
n = int(input())
m = int(input())

g = [[] for _ in range(n + 1)]
dis = [INF] * (n + 1)

for _ in range(m):
    gi, gj, gw = map(int, input().split())
    g[gi].append((gj, gw))

start, end = map(int, input().split())

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

print(dis[end])