import sys
#sys.stdin=open("input.txt", "r")
def DFS(L, sum_):
    if sum_>total//2:
        return
    else:
        if(sum_ == (total - sum_)):
            print("YES")
            sys.exit(0)
        else:
            DFS(L+1, sum_ + a[L+1])
            DFS(L+1, sum_ + a[L])
    return 

if __name__=="__main__":
    n=int(input())
    a=list(map(int, input().split()))
    total = sum(a)
    DFS(0,0)
    print("NO")


# import sys
# #sys.stdin=open("input.txt", "r")
# def DFS(L, sum):
#     if sum>total//2:
#         return
#     if L==n:
#         if sum==(total-sum):
#             print("YES")
#             sys.exit(0)
#     else:
#         DFS(L+1, sum+a[L])
#         DFS(L+1, sum)

# if __name__=="__main__":
#     n=int(input())
#     a=list(map(int, input().split()))
#     total=sum(a)
#     DFS(0, 0)
#     print("NO")

    