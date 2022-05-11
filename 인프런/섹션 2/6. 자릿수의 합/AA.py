import sys
#sys.stdin=open("./in3.txt", "r")

N = int(input())
a = list(map(int, input().split()))

def digit_sum(x):
    n_list = list(map(int, str(x)))
    return sum(n_list)

s = []

for i in range(N):
    s.append(digit_sum(a[i]))



print(a[s.index(max(s))])