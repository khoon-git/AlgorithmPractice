import sys
# sys.stdin=open("./in4.txt", "r")

if __name__=="__main__":
    n, m=map(int, input().split())
    g=[[500 for _ in range(n)] for _ in range(n)]
    for i in range(m):
        ci, cj, cc = map(int, input().split())
        g[ci - 1][cj - 1] = cc
    for k in range(n):
        for i in range(n):
            for j in range(n):
                g[i][j] = min(g[i][j], g[i][k] + g[k][j])

    for i in range(n):
        for j in range(n):
            if i == j:
                g[i][j] = 0
            if g[i][j] == 500:
                g[i][j] = "M"
            print(g[i][j], end = ' ')
        print()