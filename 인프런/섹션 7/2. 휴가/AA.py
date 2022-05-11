import sys
# sys.stdin=open("./in2.txt", "r")
def DFS(v, time, sum_score):
    global result
    if v ==  n+1:
        if result < sum_score:
            result = sum_score
    else:
        if v+a[v][0] <= n + 1:
            DFS(v+a[v][0], time + a[v][0], sum_score + a[v][1])
        DFS(v+1, time, sum_score)

        
if __name__=="__main__":
    n = int(input())
    a = list()
    res = [0, 0]
    a.append(res)
    for _ in range(n):
        a1, a2 = map(int, input().split())
        a.append([a1, a2])
    # print(a)
    result = -2147000000
    DFS(1, 0, 0)
    print(result)
    
