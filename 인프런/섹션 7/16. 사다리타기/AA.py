import sys
# sys.stdin=open("./in1.txt", "r")


def DFS(x, y):
    ch[x][y] = 1
    if x == 0:
        print(y)
    else:
        if y-1 >= 0 and a[x][y-1] == 1 and ch[x][y-1] == 0:
            DFS(x, y-1)
        elif y+1 < 10 and a[x][y+1] == 1 and ch[x][y+1] == 0:
            DFS(x, y+1)
        else:
            DFS(x-1, y)


a = [list(map(int, input().split())) for _ in range(10)]
ch = [[0]*10 for _ in range(10)]
for i in range(10):
    if a[9][i] == 2:
        DFS(9, i)
