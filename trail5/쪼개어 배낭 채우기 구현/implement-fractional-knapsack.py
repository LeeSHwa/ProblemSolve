n, m = map(int, input().split())

jewels = [tuple(map(int, input().split())) for _ in range(n)]

jewels.sort(lambda x : x[1] / x[0], reverse=True)

weight = 0
price = 0

for jewel in jewels:
    if weight + jewel[0] <= m:    
        weight += jewel[0]
        price  += jewel[1]

    else:
        price += ((m - weight)/ jewel[0]) * jewel[1]
        break

print(f"{round(price, 3):.3f}")