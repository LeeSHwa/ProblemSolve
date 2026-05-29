n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [int(input()) for _ in range(m)]

# Please write your code here.

def lower_bound(target):
    min_idx = n

    left = 0
    right = n - 1

    while right >= left:
        mid = (left + right) // 2

        if arr[mid] >= target:
            right = mid - 1
            min_idx = min(min_idx, mid)
        else:
            left = mid + 1
    
    return min_idx

def upper_bound(target):
    min_idx = n

    left = 0
    right = n - 1

    while right >= left:
        mid = (left + right) // 2

        if arr[mid] > target:
            right = mid - 1
            min_idx = min(min_idx, mid)
        else:
            left = mid + 1
    
    return min_idx

for query in queries:
    print(upper_bound(query) - lower_bound(query))
    
