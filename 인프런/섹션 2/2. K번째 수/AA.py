import sys

#sys.stdin=open("in1.txt", "rt")

T = int(input())

for i in range(T):
    N, s, e, k  = map(int, input().split())

    a = list(map(int, input().split()))
    a = a[s-1:e]
    a.sort()
    print("#%d %d" %(i+1, a[k-1]))
