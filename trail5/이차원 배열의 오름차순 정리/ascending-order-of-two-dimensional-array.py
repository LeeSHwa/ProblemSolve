def solve():
    n = int(input())
    k = int(input())

    # Please write your code here.

    left = 1
    right = n * n

    while left <= right:
        mid = (left + right) // 2
        
        cnt = 0

        for row in range(1, n + 1):
            
            col = mid // row

            cnt += min(n, col)

            if cnt >= k:
                right = mid - 1
                break
        
        if cnt < k:
            left = mid + 1

    return left

print(solve())