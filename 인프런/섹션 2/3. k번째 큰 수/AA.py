import sys

#sys.stdin=open("in1.txt", "rt")

N, K  = map(int, input().split())

a = list(map(int, input().split()))
res = set()
for i in range(len(a)):
    for j in range(i+1, len(a)):
        for k in range(j+1, len(a)):
            res.add(a[i]+ a[j]+ a[k])

b = list(res)

b.sort(reverse=True)
print(b[K-1])