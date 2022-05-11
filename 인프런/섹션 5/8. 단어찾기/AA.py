import sys
# sys.stdin=open("./in2.txt", "r")
a = int(input())
a1 = dict()
for _ in range(a):
    key = input()
    a1[key] = a1.get(key, 0) + 1
for _ in range(a-1):
    key = input()
    a1[key] -= 1

for k in a1:
    if(a1[k] != 0):
        print(k)
        break
#해쉬를 이용하여 풀기
#파이썬은 dictionary 타입이 있는데 해쉬로 구현되어있다.


# 처음 풀이방법으로 생각한 set을 이용하여 풀기
# import sys
# # sys.stdin=open("./in2.txt", "r")
# a = int(input())
# a1 = list()
# a2 = list()
# for _ in range(a):
#     a1.append(input())
# for _ in range(a-1):
#     a2.append(input())
# a1_set = set(a1)
# a2_set = set(a2)
# print(a1_set-a2_set)