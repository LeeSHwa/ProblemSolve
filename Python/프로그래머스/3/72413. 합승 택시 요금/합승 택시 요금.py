def solution(n, s, a, b, fares):

    route = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    for start, end, price in fares:
        route[start][end] = price
        route[end][start] = price
    
    for i in range(1, n + 1):
        route[i][i] = 0
        
    for via in range(1, n + 1): # 경유지
        for start in range(1, n + 1):
            for end in range(1, n + 1):
                if start == end:
                    continue
                route[start][end] = min(route[start][end], route[start][via] + route[via][end])

    min_distance = route[s][a] + route[s][b]
    
    for via in range(1, n + 1):
        min_distance = min(min_distance, route[s][via] + route[via][a] + route[via][b])
        
    return min_distance
    