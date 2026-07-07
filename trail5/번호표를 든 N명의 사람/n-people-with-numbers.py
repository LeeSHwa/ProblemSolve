import heapq

N, T_max = map(int, input().split())
ds = [int(input()) for _ in range(N)]

left = 1
right = N
answer = None

while left <= right:
    stage = []
    mid = (left + right) // 2
    flag = False # 문제없이 잘 통과했니?
    for d in ds:
        if len(stage) < mid:
            heapq.heappush(stage, d)
        
        else:
            popped = heapq.heappop(stage)
            
            if popped + d > T_max:
                # 플래그 세우기?
                flag = True
                break
            else:
                heapq.heappush(stage, d + popped)
    if flag:
        left = mid + 1
    else:
        right = mid - 1
        answer = mid
print(answer)