
import sys
# sys.stdin=open("./in1.txt", "r")
from collections import deque
n = int(input())
a = list()
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
# for i in range(n):
#         b = list(map(int, input().split()))
#         a.append(b)
# ch = [[0] * n]*n
a=[list(map(int, input().split())) for _ in range(n)]
ch=[[0]*n for _ in range(n)]
# print(a)
# print(ch)
e = n//2
dq = deque()
dq.append((e,e))
ch[e][e] = 1
L = 0
sum_apple = 0
sum_apple += a[e][e]
while True:
        if L == e:
                break
        size = len(dq)
        for i in range(size):
                tmp = dq.popleft()
                for j in range(4):
                        x = tmp[0] + dx[j]
                        y = tmp[1] + dy[j]
                        if ch[x][y] == 0:
                                ch[x][y] = 1
                                dq.append((x,y))
                                sum_apple += a[x][y]
        L += 1
print(sum_apple)