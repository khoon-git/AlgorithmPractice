from collections import deque
import sys
# sys.stdin = open("in5.txt", 'r')

n=int(input())
arr=[list(map(int, input().split())) for _ in range(n)]
dw = [[0 for _ in range(n)] for _ in range(n)]
dw[0][0] = arr[0][0]
dq = deque()
dq.append((0,0))
dx = [0, 1]
dy = [1, 0]
while dq:
    x, y = dq.popleft()
    for i in range(2):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < n and 0 <= yy < n:
            if dw[xx][yy] > 0:
                if dw[xx][yy] > arr[xx][yy] + dw[x][y]:
                    dw[xx][yy] = arr[xx][yy] + dw[x][y]
                    dq.append((xx, yy))
            else:
                dw[xx][yy] = arr[xx][yy] + dw[x][y]
                dq.append((xx, yy))

print(dw[n - 1][n - 1])
