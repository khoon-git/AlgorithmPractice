'''import sys

#sys.stdin=open("./in1.txt", "r")

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
sum = 0
for i in range(n):
    for j in range(n):
        if i < n//2:
            if n//2-i <= j <= n//2+i:
                sum += arr[i][j]
        elif i > n//2:
            if n//2-(n-i-1) <= j <= n//2+(n-i-1):
                sum += arr[i][j]
        else:
            sum += arr[i][j]

print(sum)'''
'''
답지가 더 좋은 풀이 같아서 첨부
s,e라는 변수를 두고 가운데 행까지 오기 전에는 양옆으로 퍼지고
온 후에는 양옆으로 줄어두는 알고리즘
'''
import sys
sys.stdin = open("input.txt", 'r')
n=int(input())
a=[list(map(int, input().split())) for _ in range(n)]
res=0
s=e=n//2
for i in range(n):
    for j in range(s, e+1):
        res+=a[i][j]
    if i<n//2:
        s-=1
        e+=1
    else:
        s+=1
        e-=1
print(res)

            