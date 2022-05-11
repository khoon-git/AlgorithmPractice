
import sys
# sys.stdin=open("./in1.txt", "r")
from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
a=[list(map(int, input().split())) for _ in range(7)]
dis=[[0]*7 for _ in range(7)]
dq = deque()
dq.append((0,0))
dis[0][0] = 0
while True:
        tmp = dq.popleft()
        if tmp[0] == 6 and tmp[1] == 6:
                break
        for j in range(4):
                x = tmp[0] + dx[j]
                y = tmp[1] + dy[j]
                if 6 >= x >= 0 and 6 >= y >= 0:
                        if a[x][y] == 0:
                                dis[x][y] = dis[tmp[0]][tmp[1]] + 1
                                dq.append((x,y))
if dis[6][6]==0:
    print(-1)
else:
    print(dis[6][6])