import sys

#sys.stdin=open("./in5.txt", "r")

a = list(input())

st = '0'

for i in a:
    if '0' <= i <= '9':
        st += i
print(int(st))
cnt = 0
for i in range(1, int(st)+1):
    if int(st) % i == 0:
        cnt+=1
print(cnt)
