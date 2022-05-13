import sys
# sys.stdin=open("./in3.txt", "r")
from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(m)]
dq = deque()
cnt = 0
day = 0
dq = deque()
ch = [[0]*n for _ in range(m)]
for i in range(m):
    for j in range(n):
        if a[i][j] == 1:
            dq.append((i, j))
while dq:
    x, y = dq.popleft()
    for k in range(4):
        xx = x + dx[k]
        yy = y + dy[k]
        if 0 <= xx < m and 0 <= yy < n:
            if a[xx][yy] != -1 and a[xx][yy] == 0:
                a[xx][yy] = 1
                ch[xx][yy] = ch[x][y] + 1
                dq.append((xx, yy))
flag = 1
for i in range(m):
    for j in range(n):
        if a[i][j] == 0:
            flag = 0
day = -2147000000
if flag == 1:
    for i in range(m):
        for j in range(n):
            if ch[i][j] > day:
                day = ch[i][j]
    print(day)
else:
    print(-1)
