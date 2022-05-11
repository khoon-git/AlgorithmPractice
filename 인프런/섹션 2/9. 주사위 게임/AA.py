import sys
#sys.stdin=open("./in4.txt", "r")
N = int(input())

prize = [0]*N
for i in range(N):
    a = list(map(int, input().split()))

    a.sort()

    if a[0] == a[1]:
        if a[1] == a[2]:
            prize[i] = 10000 + a[0]*1000
        else:
            prize[i] = 1000 + a[0]*100
    elif a[1] == a[2]:
        prize[i] = 1000 + a[1]*100
    else:
        prize[i] = a[2]*100

print(max(prize))
    


