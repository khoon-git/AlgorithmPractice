from itertools import combinations, permutations
import sys
# sys.stdin=open("./in1.txt", "r")
sum_list = list()
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
home_list = list()
pizza_list = list()
for i in range(n):
    for j in range(n):
        if a[i][j] == 1:
            home_list.append((i, j))
        elif a[i][j] == 2:
            pizza_list.append((i, j))
sum_ = 0
cb_pizza__list = list(combinations(pizza_list, m))
# print(cb_pizza__list)
res = 2147000000
tmp = 0
for i in cb_pizza__list:
    sum_ = 0
    for j in home_list:
        res_tmp = 2147000000
        for k in i:
            tmp = abs(j[0] - k[0]) + abs(j[1] - k[1])
            if res_tmp > tmp:
                res_tmp = tmp
        sum_ += res_tmp
    if res > sum_:
        res = sum_    
print(res)