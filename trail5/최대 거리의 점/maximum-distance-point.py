n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

arr.sort()

left  = 1
right = arr[-1] - arr[0]

while left <= right:
    mid = (left + right) // 2
    
    pre = arr[0]
    cnt = 2

    for idx in range(1, n - 1):
    
        if pre + mid <= arr[idx] <= arr[-1] - mid:
            cnt += 1
            pre = arr[idx]
     
    # print(cnt, left, right, mid)

    if cnt >= m:
        left = mid + 1
    else:
        right = mid - 1


print(left - 1)
                