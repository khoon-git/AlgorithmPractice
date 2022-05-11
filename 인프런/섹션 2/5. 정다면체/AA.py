import sys
#sys.stdin=open("./in3.txt", "r")
N, M=map(int, input().split())

a = []
for i in range(N, 0, -1):
    for j in range(M, 0, -1):
        a.append(i+j)
b = {}

for i in a:
    b[i] = b.get(i, 0) + 1

bdict = sorted(b.items(),  key = lambda item: item[1], reverse=True)

k = 0

for i in range(0, len(bdict)):
    if bdict[i][1] != bdict[i+1][1]:
        k = i
        break

for i in range(k, -1, -1):
    print(bdict[i][0], end=' ')


'''
import sys
sys.stdin=open("input.txt", "r")
n, m=map(int, input().split())
cnt=[0]*(n+m+3)
max=0
for i in range(1, n+1):
    for j in range(1, m+1):
        cnt[i+j]=cnt[i+j]+1

for i in range(n+m+1):
    if cnt[i]>max:
        max=cnt[i]
    
for i in range(n+m+1):
    if cnt[i]==max:
        print(i, end=' ')
'''