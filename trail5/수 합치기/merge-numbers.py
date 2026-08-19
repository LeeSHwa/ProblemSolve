import heapq

n = int(input())
nums = list(map(int, input().split()))
heapq.heapify(nums)

cost = 0

for _ in range(n - 1):
    a, b = heapq.heappop(nums), heapq.heappop(nums)
    heapq.heappush(nums, a + b)
    cost += a + b
    
print(cost)