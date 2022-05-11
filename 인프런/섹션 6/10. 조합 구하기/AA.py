import sys
from itertools import combinations
# sys.stdin=open("./in2.txt", "r")

    
if __name__=="__main__":
    n, m = map(int, input().split())
    res = list(int(x) for x in range(1, n + 1))
    cnt = 0
    for i in combinations(res, m):
        for j in i:
            print(j , end = ' ')
        print()
        cnt += 1
    print(cnt)
