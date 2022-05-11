
import sys
# sys.stdin=open("./in1.txt", "r")
n = int(input())
a=list(map(int, input().split()))
res = list(0 for _ in range(n))
for i in range(len(a)):
    for j in range(len(res)):
        if(res[j] == 0 and a[i] == 0):
            res[j] = i + 1
            break;
        elif(res[j] == 0):
            a[i] -= 1
for x in res:
    print(x, end='')


# 역수열 문제는 인수 i의 시작점을 어떻게 줄건지를 생각해봐야한다.