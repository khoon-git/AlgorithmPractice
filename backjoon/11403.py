import sys
input = sys.stdin.readline

n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

for k in range(n):
    for i in range(n):
        for j in range(n):
            if a[i][k] != 0 and a[k][j] != 0:
                a[i][j] = 1

for i in range(n):
    for j in range(n):
        print(a[i][j], end = ' ')
    print()
