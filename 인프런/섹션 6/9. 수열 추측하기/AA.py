import sys
sys.stdin=open("./in2.txt", "r")
def DFS(v):
    global cnt
    if len(res) == m and sum(m) == m:
        for i in res:
            print(i, end = ' ')
        print()
        cnt += 1
    else:
        for i in range(1, n+1):
            if ch[i]:
                if ch[i] == 1:
                    continue
            ch[i] = 1
            v.append(v[i]*b[i])
            DFS(v)
            v.pop()
            ch[i] = 0
        
if __name__=="__main__":
    n, m = map(int, input().split())
    res = list()
    b=[1]*(n+1)
    ch=[0]*(n+1)
    for i in range(1, n):
        b[i]=b[i-1]*(n-i)//i
    DFS(res)
    
