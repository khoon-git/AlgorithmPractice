import sys

#sys.stdin=open("./in1.txt", "r")

n = int(input())
'''
arr = [[]]*n

for i in range(n):
    arr[i] = list(map(int, input().split()))
'''
arr = [list(map(int, input().split())) for _ in range(n)]

sum_col = [0]*n
sum_row = [0]*n
sum_r = [0]*2

for i in range(n):
    for j in range(n):
        sum_col[i] += arr[i][j]

for j in range(n):
    for i in range(n):
        sum_row[j] += arr[i][j]

i = 0
while i < n:
    sum_r[0] += arr[i][i]
    i+=1

i = n-1
while i >= 0:
    sum_r[1] += arr[i][i]
    i-=1

max_sum = []

max_sum.append(max(sum_col))
max_sum.append(max(sum_row))
max_sum.append(max(sum_r))

print(max(max_sum))

'''
import sys
sys.stdin = open("input.txt", 'r')
n=int(input())
a=[list(map(int, input().split())) for _ in range(n)]
largest=-2147000000
for i in range(n):
    sum1=sum2=0
    for j in range(n):
        sum1+=a[i][j]
        sum2+=a[j][i]
    if sum1>largest:
        largest=sum1
    if sum2>largest:
        largest=sum2
sum1=sum2=0
for i in range(n):
    sum1+=a[i][i]
    sum2+=a[i][n-i-1]
if sum1>largest:
    largest=sum1
if sum2>largest:
    largest=sum2
print(largest)

'''