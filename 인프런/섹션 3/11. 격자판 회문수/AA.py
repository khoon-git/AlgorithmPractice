import sys
#sys.stdin = open("./input.txt", 'r')

a=[list(map(int, input().split())) for _ in range(7)]

def check(a):
    for i in range(2):
        if a[i] != a[4-i]:
            return False
    return True

cnt = 0

for i in range(7):
    for j in range(3):
        a_col = []
        a_row = []
        #print('%d %d %d %d' %(i, j, a[i][j], a[j][i]))
        for k in range(5):
            a_col.append(a[i][j+k])
            a_row.append(a[j+k][i])
        if check(a_col):
            cnt+=1
        if check(a_row):
            cnt+=1
print(cnt)