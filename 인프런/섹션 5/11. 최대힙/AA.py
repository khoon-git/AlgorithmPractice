import heapq
import sys
# sys.stdin=open("./in4.txt", "r")
a = int(input())
ck = []
while a != -1:
    if a == 0:
        if ck:
            print(-heapq.heappop(ck))
        else:
            print(-1)
    else:
        heapq.heappush(ck, -a)
    a = int(input())
