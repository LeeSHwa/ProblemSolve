n, m = map(int, input().split())

arr = [int(input()) for _ in range(m)]

left = min(arr)

right = max(arr) * n


while left <= right:
    mid = (left + right) // 2
    
    cnt = 0
    flag = True

    for elem in arr:
        cnt += mid // elem

        if cnt >= n:
            right = mid - 1
            flag = False
    
    if flag:
        left = mid + 1

print(left)