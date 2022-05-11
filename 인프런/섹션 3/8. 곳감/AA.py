import sys
#sys.stdin = open("./input.txt", 'r')
n=int(input())
a=[list(map(int, input().split())) for _ in range(n)]

k=int(input())
for _ in range(k):
    control = list(map(int, input().split()))
    i = control[0]-1
    if control[1] == 0:
        for _ in range(control[2]):
            arr = a[i]
            l = arr[1:n]
            r = arr[0:1]
            a[i] = l + r
            '''
            a[i].append(a[i].pop(0)) -> 따로 생각해본 방법
            '''
    else:
        for _ in range(control[2]):
            arr = a[i]
            l = arr[n-1:n]
            r = arr[0:n-1]
            a[i] = l + r
            '''
            a[i].insert(0, a[i].pop())
            '''

res = 0
s=0
e=n
for i in range(n):
    for j in range(s, e):
        res += a[i][j]
    if i<n//2:
        s+=1
        e-=1
    else:
        s-=1
        e+=1

print(res)

            