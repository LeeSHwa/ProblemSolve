from collections import defaultdict, deque

def solution(n, s, a, b, fares):
    can_go = defaultdict(list)
    
    route = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    for start, end, price in fares:
        route[start][end] = price
        route[end][start] = price
        can_go[start].append(end)
        can_go[end].append(start)
        
        
    for transit in range(1, n + 1): # 경유지
        for start in range(1, n + 1):
            for end in range(1, n + 1):
                if start == end:
                    route[start][end] = 0
                    continue
                route[start][end] = min(route[start][end], route[start][transit] + route[transit][end])

    
    # distance(start, tranist) + distance(transit, a) + distance(transit, b)
    # bfs로 transit를 다 돌아봐야하나?
    # 그래서 최소값을 갱신?
    min_distance = route[s][a] + route[s][b]
    
    q = deque()
    q.append(can_go[s])
    
    visited = [False] * (n + 1)
    visited[s] = True
    
    while q:
        nexts = q.popleft()
        
        for nxt in nexts:
            if not visited[nxt]:
                min_distance = min(min_distance, route[s][nxt] + route[nxt][a] + route[nxt][b])
                visited[nxt] = True
                
                if can_go[nxt]:
                    q.append(can_go[nxt])
    
    return min_distance
    