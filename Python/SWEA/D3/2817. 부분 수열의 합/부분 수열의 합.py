t = int(input())

for tc in range(1, t+1):
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    nums.sort()
    cnt = 0

    def backtrack(idx, prev_sum):
        global cnt
        
        if prev_sum == k:
            cnt += 1
        
        if prev_sum > k:
            return
            
        if idx == n:
            return
		
        curr_sum = prev_sum + nums[idx]
        
        if curr_sum <= k:
        	backtrack(idx + 1, curr_sum)
        else:
            return
        
        backtrack(idx + 1, prev_sum)
            
    
    backtrack(0, 0)
    print(f'#{tc} {cnt}')