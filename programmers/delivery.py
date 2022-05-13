#https://programmers.co.kr/learn/courses/30/lessons/12978
import heapq
INF = int(1e9)

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

def solution(N, road, K):
    global dis, g
    answer = 0
    g = [[] for i in range(N + 1)]
    dis = [INF] * (N + 1)
    start = 1
    for i in range(len(road)):
        gi, gj, gw = road[i][0], road[i][1], road[i][2]
        g[gi].append((gj, gw))
        g[gj].append((gi, gw))

    dijkstra(start)
    for i in range(1, N+1):
        if dis[i] <= K:
            answer += 1
    return answer


