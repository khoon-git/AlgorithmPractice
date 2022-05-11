import sys

sys.stdin=open("./in1.txt", "rt")

N = int(input())

a = list(map(int, input().split()))

av = int((sum(a) / N)+0.5)
print(av, end=' ')
aw = []
for v in a:
    aw.append(abs(av-v))

print(aw.index(min(aw))+1)
'''
이렇게 하면 평균값과 비교했을 때 똑같은 차이지만 큰수 작은수를 비교해서
작은수로 갈수없다
'''
import sys
#sys.stdin=open("input.txt", "r")
n=int(input())
a=list(map(int, input().split()))
ave=sum(a)/n
ave=ave+0.5
ave=int(ave)
min=2147000000
for idx, x in enumerate(a):
    tmp=abs(x-ave)
    if tmp<min:
        min=tmp
        score=x
        res=idx+1
    elif tmp==min:
        if x>score:
            score=x
            res=idx+1
print(ave, res)


'''
round 와 round_half_even의 차이
4.5일 때 round 를 사용하면 -> 4가 된다
따라서 이 경우 0.5를 더해준 후 int로 형변환해준다
'''