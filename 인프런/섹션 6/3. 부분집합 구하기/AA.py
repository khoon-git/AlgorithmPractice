import sys
#sys.stdin=open("input.txt", "r")
def DFS(v):
    if v==n+1:
        for i in range(1, n+1):
            if ch[i]==1:
                print(i, end=' ')
        print()
    else:
        ch[v]=1
        DFS(v+1)
        ch[v]=0
        DFS(v+1)

if __name__=="__main__":
    n=int(input())
    ch=[0]*(n+1)
    DFS(1)
    

# import sys
# sys.stdin=open("./in1.txt", "r")
# def DFS(x):
#     if x==0:
#         return
#     else:
#         for i in range(1,x):
#             print(i , end=' ')
#         DFS(x-1)
#         print()
        

# n=int(input())
# DFS(n)
