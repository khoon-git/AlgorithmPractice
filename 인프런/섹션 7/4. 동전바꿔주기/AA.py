import sys
sys.stdin=open("./in2.txt", "r")
def DFS(L, sum):
    global cnt
    if sum > T:
        return
    if L == k:
        if sum == T:
            cnt += 1
    else:
        for i in range(ns[L]+1):
            DFS(L + 1, sum + (ps[L]*i))

        
if __name__=="__main__":
    T = int(input())
    k = int(input())
    ps = list()
    ns = list()
    for i in range(k):
        a, b = map(int, input().split())
        ps.append(a)
        ns.append(b)
    cnt = 0
    DFS(0, 0)
    print(cnt)