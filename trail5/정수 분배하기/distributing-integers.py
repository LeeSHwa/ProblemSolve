n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

# Please write your code here.

ans = 0

def solve(target):
    
    cnt = 0

    for num in arr:
        cnt += num // target
    
    return cnt >= m

left = 1
right = max(arr)

while left <= right:
    mid = (left + right) // 2

    if solve(mid):
        left = mid + 1
        ans = mid
    else:
        right = mid - 1

print(ans)