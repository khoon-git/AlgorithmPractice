import sys

#sys.stdin = open("./in3.txt", "r")

N, k = map(int, input().split())

a = list()

for _ in range(N):
    a.append(int(input()))

a.sort(reverse=True)

rt = a[0]
lt = 1
answer = []
while lt <= rt:
    mid = (lt+rt)//2
    cnt = 0
    for i in a:
        cnt += (i//mid)
    if cnt >= k:
        answer.append(mid)
        lt = mid + 1
    else:
        rt = mid - 1

print(max(answer))

    


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

