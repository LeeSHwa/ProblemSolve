n = int(input())
grid = []
nums = set()

for _ in range(n):
    line = list(map(int, input().split()))
    grid. append(line)
    
    for elem in line:
        nums.add(elem)

nums = sorted(list(nums))

start = grid[0][0]

# memo : 최소값이 L일때 가장 작은 최대값
memo = []

ans = float('inf')

def init(lower):
    global memo
    memo = [[float('inf')] * n for _ in range(n)]

    memo[0][0] = grid[0][0]

    for col in range(1, n):
        if grid[0][col] >= lower:
            memo[0][col] = max(memo[0][col - 1], grid[0][col])
        else:
            break

    for row in range(1, n):
        if grid[row][0] >= lower:
            memo[row][0] = max(memo[row - 1][0], grid[row][0])
        else:
            break





def dp(lower, row, col):

    for dr, dc in [(1, 0), (0, 1)]:
        nr = row + dr
        nc = col + dc

        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] >= lower:

            memo[nr][nc] = max(grid[nr][nc], min(memo[nr - 1][nc], memo[nr][nc - 1], memo[nr][nc]))

            dp(lower, nr, nc)




for lower in nums:
    if lower > start:
        break
    init(lower)
    

    dp(lower, 0, 0)

    if memo[n-1][n-1] != float('inf'):
        ans = min(ans, memo[n-1][n-1] - lower)

print(ans)