import sys
# sys.stdin=open("./in2.txt", "r")
def DFS(v, sum_):
    if v == n:
        if sum(a) >= sum_ > 0:
            res.add(sum_)
    else:
        DFS(v+1, sum_+a[v])
        DFS(v+1, sum_-a[v])
        DFS(v+1, sum_)

        
if __name__=="__main__":
    n = int(input())
    a = list(map(int, input().split()))
    res=set()
    DFS(0, 0)
    print(sum(a)-len(res))
