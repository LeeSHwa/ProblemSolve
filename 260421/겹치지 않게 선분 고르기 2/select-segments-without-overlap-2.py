n = int(input())

line = {}
MAX_RANGE = 1001

dp = [0] * MAX_RANGE

for _ in range(n):
    x1, x2 = map(int, input().split())

    if x1 in line:
        line[x1] = min(line[x1], x2)
    else:
        line[x1] = x2

pos = sorted(line.items(), key = lambda x : x[1])

for x1, x2 in pos:
    
    max_value = 0
    for end in range(x1):
        max_value = max(max_value, dp[end])
    
    dp[x2] = max_value + 1

print(max(dp))
    