import sys
# sys.stdin=open("./in4.txt", "r")
n = int(input())
a = list(map(int, input().split()))
rest = int(input())
dr = [1000 for _ in range(rest + 1)]
dr[0] = 0
for _ in range(n):
    for k in a:
        for j in range(k, rest + 1):
            dr[j] = min(dr[j], dr[j - k] + 1)
print(dr[rest])


# import sys
# sys.stdin=open("./in4.txt", "r")
# def DFS(v, sum):
#     global result
#     if v >= result:
#         return
#     if rest == sum:
#         if result > v:
#             result = v
#     if sum > rest:
#         return
#     else:
#         for i in range(n):
#             DFS(v+1, sum + a[i])


# if __name__ == "__main__":
#     n = int(input())
#     a = list(map(int, input().split()))
#     rest = int(input())
#     result = 2147000000
#     a.sort(reverse=True)
#     DFS(0, 0)
#     print(result)
