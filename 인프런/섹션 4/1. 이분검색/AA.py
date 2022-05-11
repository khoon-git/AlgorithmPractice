import sys

#sys.stdin = open("./in1.txt", "r")

N, n = map(int, input().split())

a = list(map(int, input().split()))

a.sort()

rt = N
lt = 0
while True:
    mid = (lt+rt)//2
    if a[mid] == n:
        print(mid+1)
        break
    elif a[mid] > n:
        rt = mid + 1
    else:
        lt = mid
    

'''import sys

sys.stdin = open("./in1.txt", "r")

N, n = map(int, input().split())

a = list(map(int, input().split()))

a.sort()

def find_x(a, n):
    mid = len(a)//2
    print(a)
    for i, v in enumerate(a):
        print('%d %d' %(a[mid], n))
        if a[mid] == n:
            print(i)
            return i
        elif a[mid] > n:
            find_x(a[0:mid], n)
        else:
            find_x(a[mid:len(a)], n)

print(find_x(a,n))'''

