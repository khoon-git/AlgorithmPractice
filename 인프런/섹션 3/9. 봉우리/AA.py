import sys
#sys.stdin = open("./in1.txt", 'r')
n=int(input())

a = []

a.append(list([0]*(n+2)))

for _ in range(n):
    a.append(list(map(int, input().split())))

a.append(list([0]*(n+2)))

cnt = 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
for i in range(1, n+1):
    a[i].insert(0, 0)
    a[i].insert(n+1, 0)

for i in range(1, n+1):
    for j in range(1, n+1):
        if all(a[i][j] > a[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt+=1
        '''if a[i-1][j] < a[i][j] and a[i+1][j] < a[i][j] and a[i][j-1] < a[i][j] and a[i][j+1] < a[i][j]:
            #print('%d %d' %(i, j))
            cnt += 1'''

print(cnt)