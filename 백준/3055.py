from collections import deque
n, m = map(int, input().split())
a = [list() for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for i in range(n):
    str_ = input()
    for k in str_:
        a[i].append(k)
dw = deque()
dd = deque()
ch = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if a[i][j] == '*':
            dw.append((i, j))
        elif a[i][j] == 'D':
            ep = (i, j)
        elif a[i][j] == 'S':
            dd.append((i, j))

while True:
    if len(dw) == 0 and len(dd) == 0:
        break
    cnt = len(dw)
    while cnt != 0:
        x, y = dw.popleft()
        for k in range(4):
            xx = x + dx[k]
            yy = y + dy[k]
            if 0 <= xx < n and 0 <= yy < m:
                if a[xx][yy] != 'X' and a[xx][yy] != '*' and a[xx][yy] != 'D':
                    a[xx][yy] = '*'
                    dw.append((xx, yy))
        cnt -= 1
    cnt = len(dd)
    while cnt != 0:
        x, y = dd.popleft()
        for k in range(4):
            xx = x + dx[k]
            yy = y + dy[k]
            if 0 <= xx < n and 0 <= yy < m:
                if a[xx][yy] != 'X' and a[xx][yy] != '*' and a[xx][yy] != 'S':
                    a[xx][yy] = 'S'
                    ch[xx][yy] = ch[x][y] + 1
                    dd.append((xx, yy))
        cnt -= 1
if ch[ep[0]][ep[1]] == 0:
    print("KAKTUS")
else:
    print(ch[ep[0]][ep[1]])
