
import sys
# sys.stdin=open("./in4.txt", "r")
def DFS(v, sum):
    global result
    if v>=result:
        return
    if rest == sum:
        if result > v:
            result = v
    if sum > rest:
        return
    else:
        for i in range(n):
            DFS(v+1, sum + a[i])
        
if __name__=="__main__":
    n = int(input())
    a = list(map(int, input().split()))
    rest = int(input())
    result = 2147000000
    a.sort(reverse=True)
    DFS(0, 0)
    print(result)
    
