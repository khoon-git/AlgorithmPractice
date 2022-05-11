import sys
#sys.stdin=open("./in1.txt", "r")
N = int(input())
a = list(map(int, input().split()))

res = 0
score = 0
for i in range(N):
    if a[i] == 1:
        res += 1
        score += res
    else:
        res = 0
    
    

print(score)
    


