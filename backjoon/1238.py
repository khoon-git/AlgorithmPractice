import sys
input = sys.stdin.readline
INF = int(1e9)
import heapq
n, m, x = map(int, input().split())
g = [[] for _ in range(n + 1)]
dis = [INF for _ in range(n + 1)]
for _ in range(m):
    gi, gj, gw = map(int, input().split())
    g[gi].append((gj, gw))
def dijkstar(start):
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if dis[now] < dist:
            continue
        for i in g[now]:
            cost = dist + i[1]
            if dis[i[0]] > cost:
                dis[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

res = [0 for _ in range(n+1)]

for i in range(1, n+1):
    dis = [INF for _ in range(n + 1)]
    dis[i] = 0
    dijkstar(i)
    if i == x:
        for j in range(1, len(dis)):
            res[j] += dis[j]
    else:
        res[i] += dis[x]
print(max(res))