## Bottom-up 방법

import sys
sys.stdin = open("./in1.txt", 'r')
n=int(input())
dy = [0]*(n+1)
dy[1] = 1
dy[2] = 2

for i in range(3, n+1):
    dy[i] = dy[i-1] + dy[i-2]

print(dy[n])

## Top-Down 방법

import sys
sys.stdin = open("./in1.txt", 'r')
n = int(input())
def DFS(len):
    if dy[len]>0:
        return dy[len]
    if len==1 or len==2:
        return len
    else:
        dy[n] = DFS(len-1)+DFS(len-2)
        return dy[len]


if __name__ == "__main__":
    n = int(input())
    dy = [0]*(n+1)
    print(DFS(n))
