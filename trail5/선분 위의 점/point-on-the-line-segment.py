n, m = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

def upper_bound(target):
    left = 0
    right = n - 1

    min_idx = n

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] > target:
            right = mid - 1
            min_idx = min(min_idx, mid)
        else:
            left = mid + 1
    
    return min_idx

def under_bound(target):
    left = 0
    right = n - 1

    max_idx = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] < target:
            left = mid + 1    
            max_idx = max(max_idx, mid)
        else:
            right = mid - 1

    return max_idx

for _ in range(m):
    start, end = map(int, input().split())

    print(upper_bound(end) - under_bound(start) - 1)