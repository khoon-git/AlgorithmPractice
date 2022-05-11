
import sys
# sys.stdin=open("./in2.txt", "r")
from collections import deque
n, m= map(int, input().split())
a_l = list(map(int, input().split()))
a=deque()
for i in range(n):
    test = [a_l[i], i]
    a.append(test)
cnt = 1
while a:
    res = a.popleft()
    max_t = max(a)
    if(res[0] >= max_t[0]):
        if res[1] == m:
            print(cnt)
            break
        cnt += 1
    else:
        a.append(res)


