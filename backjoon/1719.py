import sys
#sys.stdin("./in1.txt")

n, m = map(int, input().split())
g = [[sys.maxsize for _ in range(n)] for _ in range(n)]
result = [[x for x in range(n)] for _ in range(n)]
for _ in range(m):
    gi, gj, gw = map(int, input().split())
    g[gi - 1][gj - 1] = gw
    g[gj - 1][gi - 1] = gw

for k in range(n):
    for i in range(n):
        for j in range(n):
            if g[i][j] > g[i][k] + g[k][j]:
                g[i][j] = g[i][k] + g[k][j]
                result[i][j] = result[i][k]

for i in range(n):
    for j in range(n):
        if i == j:
            print("-", end = ' ')
        else:
            print(result[i][j] + 1, end = ' ')
    print()
