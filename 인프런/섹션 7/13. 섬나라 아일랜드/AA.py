import sys
# sys.stdin=open("./in1.txt", "r")
from collections import deque
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
n = int(input())
a=[list(map(int, input().split())) for _ in range(n)]
dq = deque()
cnt = 0
for i in range(n):
    for j in range(n):
        if a[i][j] == 1:
            a[i][j] = 0
            dq.append((i, j))
            while dq:
                tmp = dq.popleft()
                x = tmp[0]
                y = tmp[1]
                for k in range(8):
                    xx = x + dx[k]
                    yy = y + dy[k]
                    if xx < 0 or xx >= n or yy < 0 or yy >= n or a[xx][yy] == 0:
                        continue
                    else:
                        a[xx][yy] = 0
                        dq.append((xx, yy))
            cnt += 1

print(cnt)