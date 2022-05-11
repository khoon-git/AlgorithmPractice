import sys
#sys.stdin=open("./in1.txt", "r")
N = int(input())

a = list(map(int, input().split()))

def reverse(x):
    return int((str(x)[::-1]))

def isPrime(x):
    if x == 1:
        return 0
    for i in range(2, x//2+1):
        if x%i == 0:
            return 0
    return 1
        
for i in a:
    if isPrime(reverse(i)) == 1:
        print(reverse(i), end=' ')


'''
ifPrime의 for문 조건이 절반만 되도 됨
ex 16 = 1*16 다음에 2*"8" 이기때문에!
'''