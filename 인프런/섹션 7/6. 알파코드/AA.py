# import sys
# sys.stdin=open("./in1.txt", "r")
# from string import ascii_uppercase
# def DFS(L, res):
#     global cnt
#     if L == n:
#         print(''.join(ch))
#         cnt += 1
#     else:
#         if 1 <= int(res + code[L+1]) and int(res + code[L+1]) <= 26:
#             ch.append(chr(int(res)+64))
#             DFS(L+1, code[L+1])
#             ch.pop()
#             ch.append(chr(int(res)+64))
#             DFS(L+1, res+code[L+1])
#         else:
#             ch.append(chr(int(res)+64))
#             DFS(L+1, code[L+1])
#             ch.pop()
        
# if __name__=="__main__":
#     code=list(map(int, input()))
#     n=len(code)
#     code.insert(n, -1)
#     cnt=0
#     ch = list()
#     DFS(0, code[0])
#     print(cnt)
from string import ascii_uppercase


def dfs(a, alpha):
    global cnt, lst
    if a >= m:
        lst.append(alpha)
        cnt += 1
    else:
        if int(n[a]) == 0:
            return
        dfs(a + 1, alpha + alpha_up[int(n[a]) - 1])
        val = int(n[a:a+2])
        if a < m - 1 and val <= 26:
            dfs(a + 2, alpha + alpha_up[val - 1])


alpha_up = ascii_uppercase
n = input()
m = len(n)
cnt = 0
lst = []
dfs(0, "")
lst.sort()
print("\n".join(lst) + "\n" + str(cnt))