import sys
# sys.stdin = open("in1.txt", 'r')
n=int(input())
arr=[list(map(int, input().split())) for _ in range(n)]
dy=[0]*n
arr.sort(reverse=True)
dy[0] = arr[0][1]
res = arr[0][1]
for i in range(1, n):
    max = 0
    for j in range(i-1, -1, -1):
        if arr[j][2] > arr[i][2] and max < dy[j]:
            max = dy[j]
    dy[i] = max + arr[i][1]
    if dy[i] > res:
        res = dy[i]

print(res)