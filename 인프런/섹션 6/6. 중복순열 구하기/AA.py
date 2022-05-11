
import sys
# sys.stdin=open("./in4.txt", "r")
def DFS(v):
    global cnt
    if len(v) == m:
        for i in v:
            print(i, end=' ')
        print()
        cnt += 1
    else:
        for i in range(1, n+1): 
            v.append(i)
            DFS(v)
            v.pop()
        
if __name__=="__main__":
    n, m = map(int, input().split())
    cnt = 0
    v = list()
    DFS(v)
    print(cnt)
    
