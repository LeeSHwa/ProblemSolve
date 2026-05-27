n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [int(input()) for _ in range(m)]

# Please write your code here.


def find_idx(target):
    left = 0
    right = n - 1

    while right >= left:
        mid = (right + left) // 2
        
        if arr[mid] == target:
            return mid + 1
        
        if arr[mid] > target:
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
    
    return -1
    

for target in queries:
    print(find_idx(target))
    