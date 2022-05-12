import sys
# sys.stdin=open("./in1.txt", "r")
n, m = map(int, input().split())
dw = [0 for _ in range(m + 1)]
for _ in range(n):
    j, w = map(int, input().split())
    for k in range(m, w-1, -1):
        dw[k] = max(dw[k], dw[k-w]+j)
print(dw[m])

# if __name__ == "__main__":
#     n, m = map(int, input().split())
#     dy = [0]*(m+1)
#     for i in range(n):
#         ps, pt = map(int, input().split())
#         for j in range(m, pt-1, -1):
#             dy[j] = max(dy[j], dy[j-pt]+ps)
#     print(dy[m])



# import sys
# sys.stdin=open("./in4.txt", "r")
# def DFS(L, sum_score, sum_t):
#     global result
#     if m < sum_t:
#         return
#     if L == n:
#         if result < sum_score:
#             result = sum_score
#     else:
#         DFS(L+1, sum_score + a[L][0], sum_t + a[L][1])
#         DFS(L+1, sum_score, sum_t)


# if __name__ == "__main__":
#     n, m = map(int, input().split())
#     a = list()
#     for i in range(n):
#         a.append(list(map(int, input().split())))
#     result = -2147000000
#     DFS(0, 0, 0)
#     print(result)
