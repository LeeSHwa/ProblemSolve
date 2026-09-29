def solution(triangle):
    answer = 0
    n = len(triangle)
    
    for floor in range(1, n):
        for idx in range(floor + 1):
            if idx == 0:
                triangle[floor][idx] += triangle[floor - 1][idx]
            elif idx == floor:
                triangle[floor][idx] += triangle[floor - 1][floor - 1]
            else:    
                triangle[floor][idx] = max(triangle[floor][idx] + triangle[floor - 1][idx], triangle[floor][idx] + triangle[floor - 1][idx - 1])

    answer = max(triangle[n - 1])
    
    return answer