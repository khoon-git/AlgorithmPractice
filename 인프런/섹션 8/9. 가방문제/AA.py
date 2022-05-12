from collections import deque
import sys
# sys.stdin = open("in5.txt", 'r')
n, m = map(int, input().split())
dw = [0 for _ in range(m + 1)]
for _ in range(n):
    j, w = map(int, input().split())
    for k in range(j, m + 1):
        dw[k] = max(dw[k], dw[k-j]+w)
print(dw[m])