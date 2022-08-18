import sys

input = sys.stdin.readline

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    m = int(input())
    if max(arr)*n <= m:
        print(max(arr))
        return
    l = 1
    r = max(arr)
    answer = l
    
    while l <= r:
        sum_ = 0
        mid = (l + r) // 2
        for i in arr:
            if i >= mid:
                sum_ += mid
            else:
                sum_ += i
                
        if sum_ <= m:
            l = mid + 1
            answer = mid
        else:
            r = mid - 1

    print(answer)

if __name__ == "__main__":
    main()