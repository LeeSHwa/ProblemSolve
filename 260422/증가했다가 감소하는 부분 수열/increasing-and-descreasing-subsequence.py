n = int(input())

nums = list(map(int, input().split()))

# 상태 기록 / 0 : 상승 / 1: 하강

dp = [[-1, 1] for _ in range(n)] # [정해지지 않은 상태, 기본 1]

ans = -1

for i in range(1, n):
    
    for j in range(i):
        # 1. nums[i]가 이전 값들보다 클 때. 하향추세였나 확인
        if nums[i] > nums[j]:
            if dp[j][0] == 1:
                continue
            else:
                dp[i] = [0, max(dp[i][1], dp[j][1] + 1)]
        
        elif nums[i] < nums[j]:
            if dp[j][1] >= dp[i][1]:
                dp[i] = [1, dp[j][1] + 1]

    ans = max(ans, dp[i][1])
    
print(ans)