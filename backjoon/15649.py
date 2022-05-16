import sys
input = sys.stdin.readline


def DFS(L):
    global cnt
    if L == m:
        for i in range(m):
            print(res[i], end=' ')
        print()
        cnt += 1
    else:
        for i in range(1, n+1):
            if ch[i] == 0:
                ch[i] = 1
                res[L] = i
                DFS(L+1)
                ch[i] = 0
        
if __name__=="__main__":
    n, m = map(int, input().split())
    res = list(x for x in range(1, n + 1))
    cnt = 0
    ch = [0] * (n + 1)
    DFS(0)