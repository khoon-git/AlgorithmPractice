
import sys
# sys.stdin=open("./in4.txt", "r")
def DFS(v, sum_score, time):
    global result
    if time > m:
        return
    if v == n:
        if result < sum_score:
            result = sum_score
    else:
        DFS(v+1, sum_score + a[v][0], time + a[v][1])
        DFS(v+1, sum_score, time)

        
if __name__=="__main__":
    n, m = map(int, input().split())
    a = list()
    for _ in range(n):
        a1, a2 = map(int, input().split())
        a.append([a1, a2])
    # print(a)
    result = -2147000000
    DFS(0, 0, 0)
    print(result)
    

