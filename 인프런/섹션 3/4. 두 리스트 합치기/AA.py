'''
import sys

#sys.stdin=open("./in1.txt", "r")

N = int(input())
a = list(map(int, input().split()))
M = int(input())
b = list(map(int, input().split()))
arr = a+b
arr.sort()
for i in arr:
    print(i, end=' ')
-> 내가 짠것 nlogn시간복잡도
'''
'''
-> n의 시간복잡도를 가진 코드
'''
import sys
N = int(input())
a = list(map(int, input().split()))
M = int(input())
b = list(map(int, input().split()))

p1 = p2 = 0
arr = []

while p1 < N and p2 < M:
    if a[p1] > b[p2]:
        arr.append(b[p2])
        p2 += 1
    else :
        arr.append(a[p1])
        p1 += 1

if p1 < N:
    arr = arr+a[p1:]
else:
    arr = arr+b[p2:]
for i in arr:
    print(i, end=' ')







