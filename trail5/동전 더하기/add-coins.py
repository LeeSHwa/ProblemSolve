n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

cnt = 0

for i in range(n - 1, -1, -1):
    coin = k // coins[i]
    if coin > 0:
        cnt += coin
        k -= coin * coins[i]
    
    if k == 0:
        break

print(cnt)