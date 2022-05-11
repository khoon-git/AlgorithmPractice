
import sys
# sys.stdin=open("./in4.txt", "r")
from collections import deque
s, e = map(int, input().split())
maxi = 10000
dis = [0] * (maxi+1)
ch = [0] * (maxi+1)
dq = deque()
ch[s] = 1
dis[s] = 0
dq.append(s)
while dq:
    tmp = dq.popleft()
    if tmp == e:
        break
    for i in (tmp + 1, tmp - 1, tmp + 5):
        if 0 < i <= maxi:
            if ch[i] == 0:
                dq.append(i)
                ch[i] = 1   
                dis[i] = dis[tmp] + 1
print(dis[e])