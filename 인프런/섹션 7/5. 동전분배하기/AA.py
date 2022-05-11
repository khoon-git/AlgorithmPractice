import sys
sys.stdin=open("./in1.txt", "r")
def DFS(L):
    global res
    if L == N:
        test = set(ch)
        if len(test) == 3:
            if res > max(test)-min(test):
                # print(test)
                res = max(test)-min(test)
    else:
        for i in range(3):
            ch[i] += a[L]
            DFS(L + 1)
            ch[i] -= a[L]

        
if __name__=="__main__":
    N = int(input())
    a = list()
    ch = [0] * 3
    for i in range(N):
        a.append(int(input()))
    res = 2147000000
    DFS(0)
    print(res)