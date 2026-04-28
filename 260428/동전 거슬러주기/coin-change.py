n, m = map(int, input().split())
coins = list(map(int, input().split()))

dp = [float('inf')] * (m + 1)

for i in coins:
    dp[i] = 1

for i in range(1, m + 1):

    for coin in coins:
        if i - coin > 0:
            dp[i] = min(dp[i], dp[i - coin] + 1)
    
if dp[-1] == float('inf'):
    print(-1)
else:
    print(dp[-1])