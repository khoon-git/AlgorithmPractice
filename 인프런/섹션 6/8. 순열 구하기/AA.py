import sys
# sys.stdin=open("./in2.txt", "r")
def DFS(v):
    global cnt
    if len(res) == m:
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
            v.append(i)
            DFS(v)
            v.pop()
            ch[i] = 0
        
if __name__=="__main__":
    n, m = map(int, input().split())
    res = list(x for x in range(1, n + 1))
    cnt = 0
    ch = [0] * (n + 1)
    DFS(res)
    print(cnt)
    
# permutations를 사용한 풀이법
# from itertools import permutations
# if __name__=="__main__":
#     n, m = map(int, input().split())
#     res = list(int(x) for x in range(1, n + 1))
#     cnt = 0
#     for i in permutations(res, m):
#         for j in i:
#             print(j , end = ' ')
#         print()
#         cnt += 1
#     print(cnt)
