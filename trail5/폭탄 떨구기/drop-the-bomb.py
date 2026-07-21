'''
입력
7 2
20
25
18
8
10
3
1

출력
5
'''
n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()

left = 1
right = arr[-1] - arr[0]
answer = 0

while left <= right:
    mid = (left + right) // 2
    
    window = 2 * mid
    
    coverage = arr[0] + window
    
    cnt = 1
    
    for x in arr:
        if x > coverage:
            cnt += 1
            
            if cnt > k:
                break
            coverage = x + window
    
    if cnt > k:
        left = mid + 1
    else:
        right = mid - 1
        answer = mid

print(answer)