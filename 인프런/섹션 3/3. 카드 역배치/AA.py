import sys

#sys.stdin=open("./in5.txt", "r")
arr = []
for i in range(1, 21):
    arr.append(i)

for i in range(10):
    a ,b = map(int, input().split())
    a1 = arr[0:a-1]
    a2 = arr[b:20]
    ch = arr[a-1:b]
    arr = a1 + ch[::-1] + a2

for i in arr:
    print(i, end=' ')