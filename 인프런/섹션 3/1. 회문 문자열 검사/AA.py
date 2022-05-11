import sys

sys.stdin=open("./in1.txt", "r")

N = int(input())

for i in range(N):
    a = input()
    n = 0
    res = 0
    a = a.lower()
    for ch in a[:len(a)//2:-1]:
        if a[n] != ch:
            res = 1
        n += 1
    if res == 1:
        print('#%d NO' %(i+1))
    else:
        print('#%d YES' %(i+1))
