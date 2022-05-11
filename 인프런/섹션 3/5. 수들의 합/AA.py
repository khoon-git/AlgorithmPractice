import sys

#sys.stdin=open("./in1.txt", "r")

a , b = map(int, input().split())

arr = list(map(int, input().split()))

lt = 0
rt = 1
tot = arr[0]
cnt = 0

while True:
    if tot < b:
        if rt < a:
            tot += arr[rt]
            rt += 1
        else:
            break
    elif tot == b:
        cnt += 1
        tot -= arr[lt]
        lt += 1
    else :
        tot -= arr[lt]
        lt += 1
    
print(cnt)

'''
import sys

#sys.stdin=open("./in1.txt", "r")

a , b = map(int, input().split())

arr = list(map(int, input().split()))
sum = 0
cnt = 0
for i in range(a):
    sum += arr[i]
    if sum == b:
        cnt += 1
        sum = 0
        continue
    else:
        for j in range(i+1, a):
            sum += arr[j]
            if sum == b:
                cnt += 1
                sum = 0
                break
            if sum > b:
                sum = 0
                break


print(cnt)
'''




