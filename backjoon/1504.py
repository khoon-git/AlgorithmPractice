import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())

g = [[] for _ in range(n + 1)]
for _ in range(m):
    gi, gj, gw = map(int, input().split())
    g[gi].append((gj,gw))
    g[gj].append((gi,gw))

v1, v2 = map(int, input().split())

def dijkstar(start, end):
    dis = [INF for _ in range(n + 1)]
    dis[start] = 0
    q = []
    heapq.heappush(q, (dis[start], start))
    while q:
        dist, now = heapq.heappop(q)
        if dis[now] < dist:
            continue
        for i in g[now]:
            cost = dist + i[1]
            if cost < dis[i[0]]:
                dis[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return dis[end]
res = 0
if v1 == 1:
    res += dijkstar(1, v2)
    res += dijkstar(v2, n)
elif v2 == n:
    res += dijkstar(1, v1)
    res += dijkstar(v1, n)
else:
    res1 = 0
    res2 = 0
    res1 += dijkstar(1, v1)
    res1 += dijkstar(v1, v2)
    res1 += dijkstar(v2, n)
    res2 += dijkstar(1, v2)
    res2 += dijkstar(v2, v1)
    res2 += dijkstar(v1, n)
    res = min(res1, res2)

if res >= INF:
    print(-1)
else:
    print(res)