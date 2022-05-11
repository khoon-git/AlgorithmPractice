import sys
# sys.stdin=open("./in1.txt", "r")
from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n = int(input())
max_t = -2147000000
max_cnt = -2147000000
a = list()
for _ in range(n):
    b = list(map(int, input().split()))
    a.append(b)
    for j in b:
        if j > max_t:
            max_t = j
# print(a)
dq = deque()
res = list()
cnt = 0
idx = 0
dq = deque()
for idx in range(max_t):
    ch = [[0]*n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if a[i][j] > idx and ch[i][j] == 0:
                ch[i][j] = 1
                dq.append((i, j))
                while dq:
                    x, y = dq.popleft()
                    for k in range(4):
                        xx = x + dx[k]
                        yy = y + dy[k]
                        if 0 <= xx < n and 0 <= yy < n and a[xx][yy] > idx and ch[xx][yy] == 0:
                            ch[xx][yy] = 1
                            dq.append((xx, yy))
                cnt += 1
    if cnt == 0:
        break
    if max_cnt < cnt :
        max_cnt = cnt
print(max_cnt)
