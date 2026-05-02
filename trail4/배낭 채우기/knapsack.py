def solve():
    n, m = map(int, input().split())

    jewels = [tuple(map(int, input().split())) for _ in range(n)]

    UNUSED = -float('inf')

    # i번째 보석까지 고려했을 때, j의 무게에서 얻을 수 있는 최대의 가치
    dp = [[UNUSED] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = 0

    #누더기1
    # if jewels[0][0] <= m:
    #     dp[0][jewels[0][0]] = jewels[0][1]

    for i in range(1, n + 1):

        wei, price = jewels[i - 1]
        
        #누더기2
        # if m >= wei:
        #     dp[i][wei] = price

        for j in range(m + 1):
            #누더기3
            if j >= wei:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - wei] + price)

            #누더기4
            else:
                dp[i][j] = max(dp[i][j], dp[i-1][j])


    #누더기5
    return max(dp[-1])

print(solve())