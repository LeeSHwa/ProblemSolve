n = int(input())

price = list(map(int, input().split()))

dp = [0] * (n + 1)

for i in range(1, n + 1):
    
    dp[i] = price[i - 1]

    for j in range(i):
        dp[i] = max(dp[i], dp[j] + price[i - j - 1])

print(dp[-1])