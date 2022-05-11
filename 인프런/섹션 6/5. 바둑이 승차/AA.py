
import sys
# sys.stdin=open("./in4.txt", "r")


def DFS(v, sum_, tsum):
    if sum_ > c:
        return
    if sum_+(total-tsum) < max(max_list):
        return
    if v==n:
        max_list.append(sum_)
    else:
        DFS(v+1, sum_ + a[v], tsum + a[v])
        DFS(v+1, sum_ , tsum + a[v])


if __name__=="__main__":
    c , n = map(int, input().split())
    a=[0]*n
    for i in range(n):
        a[i]=int(input())
    max_list = [0]
    total = sum(a)
    DFS(0, 0, 0)
    print(max(max_list))