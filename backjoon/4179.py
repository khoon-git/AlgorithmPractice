from collections import deque
n, m = map(int, input().split())
a = [list() for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for i in range(n):
    str_ = input()
    for k in str_:
        a[i].append(k)
dj = deque()
flag = 0
df = deque()
ch = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if a[i][j] == 'J':
            if i == 0 or j == 0:
                print(1)
                flag = 1
                # print(ch)
                break
            ch[i][j] = 1
            dj.append((i, j))
        elif a[i][j] == '#':
            ch[i][j] = 1
        elif a[i][j] == 'F':
            df.append((i, j))

while True:
    if len(dj) == 0 and len(df) == 0:
        break
    if flag == 1:
        break
    cnt = len(df)
    while cnt != 0:
        x, y = df.popleft()
        for k in range(4):
            xx = x + dx[k]
            yy = y + dy[k]
            if 0 <= xx < n and 0 <= yy < m:
                if a[xx][yy] != '#' and a[xx][yy] != 'F':
                    a[xx][yy] = 'F'
                    df.append((xx, yy))
        cnt -= 1
    cnt = len(dj)
    while cnt != 0:
        x, y = dj.popleft()
        for k in range(4):
            xx = x + dx[k]
            yy = y + dy[k]
            if 0 <= xx < n and 0 <= yy < m:
                if a[xx][yy] != '#' and a[xx][yy] != 'F' and ch[xx][yy] == 0:
                    if xx == n - 1 or yy == m - 1 or xx == 0 or yy == 0:
                        if a[xx][yy] != '#' and ch[xx][yy] == 0:
                            ch[xx][yy] = ch[x][y] + 1
                            print(ch[xx][yy])
                            flag = 1
                            # print(ch)
                            break
                    ch[xx][yy] = ch[x][y] + 1
                    dj.append((xx, yy))

        cnt -= 1
        if flag == 1:
            break
if flag == 0:
    print("IMPOSSIBLE")
