import sys
# sys.stdin=open("./in4.txt", "r")

if __name__ == "__main__":
    n = int(input())
    res = 2147000
    g = [[500 for _ in range(n)] for _ in range(n)]
    while True:
        ci, cj = map(int, input().split())
        if ci == -1 and cj == -1:
            break
        g[ci - 1][cj - 1] = 1
        g[cj - 1][ci - 1] = 1
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j:
                    g[i][j] = 0
                else:
                    g[i][j] = min(g[i][j], g[i][k] + g[k][j])
    result = [0] * n
    cnt = 0
    for i in range(n):
        mt = -1
        for j in range(n):
            mt = max(mt, g[i][j])
        result[i] = mt
        if mt < res:
            res = mt
    out = list()
    for i, v in enumerate(result):
        if v == res:
            cnt += 1
            out.append(i) 
    print("{} {}".format(res, cnt))
    for i in out:
        print(i+1, end=' ')
            
    
