from collections import deque


def solution(n, edge):
    answer = 0
    a = [[] for _ in range(n+1)]
    ch = [0 for _ in range(n+1)]
    for i in edge:
        a[i[0]].append(i[1])
        a[i[1]].append(i[0])
    q = deque()
    q.append(1)
    res = [0 for _ in range(n+1)]
    res[1] = 0
    while q:
        x = q.popleft()
        for i in a[x]:
            if ch[i] == 0:
                ch[i] = 1
                q.append(i)
                res[i] = res[x] + 1

    max_t = max(res)
    for i in range(2, len(res)):
        if max_t == res[i]:
            answer += 1
    return answer


vertex = [[3, 6], [4, 3], [3, 4], [1, 3], [1, 4], [2, 4], [5, 4]]
#vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

print(solution(6, vertex))

# from collections import deque


# def solution(n, edge):
#     answer = 0
#     a = [[0 for _ in range(n+1)] for _ in range(n+1)]
#     ch = [0 for _ in range(n+1)]
#     for i in edge:
#         a[i[0]][i[1]] = 1
#         a[i[1]][i[0]] = 1
#     q = deque()
#     q.append(1)
#     res = [0 for _ in range(n+1)]
#     res[1] = 0
#     while q:
#         x = q.popleft()
#         for i in range(n + 1):
#             if a[x][i] == 1 and ch[i] == 0:
#                 ch[i] = 1
#                 q.append(i)
#                 res[i] = res[x] + 1
#     print(res)
#     max_t = max(res)
#     for i in range(2, len(res)):
#         if max_t == res[i]:
#             answer += 1
#     return answer