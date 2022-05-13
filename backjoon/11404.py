import sys
input = sys.stdin.readline

INF = int(1e9)
n = int(input())
m = int(input())
g = [[sys.maxsize for _ in range(n)] for _ in range(n)]
for _ in range(m):
    gi, gj, gw = map(int, input().split())
    if gi == gj:
        g[gi -1][gj - 1] = 0
    else:
        g[gi - 1][gj - 1] = min(g[gi - 1][gj - 1], gw)


for k in range(n):
    for i in range(n):
        for j in range(n):
            g[i][j] = min(g[i][j], g[i][k] + g[k][j])


for i in range(n):
    for j in range(n):
        if i == j:
            print(0, end = ' ')
        else:
            if g[i][j] >= sys.maxsize:
                print(0, end = ' ')
            else:
                print(g[i][j], end = ' ')
    print()