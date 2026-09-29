def solution(n):
    answer = []
    LIMIT = (n * (n + 1)) // 2 # 카운터가 여까지 도달하면 종료
    
    tri = [[0] * i for i in range(1, n + 1)]
    tri[0][0] = 1
    
    dirs = [(1, 0), (0, 1), (-1, -1)]
    dir = 0
    counter = 2
    r, c = 0, 0
    
    while counter <= LIMIT:
        dr, dc = dirs[dir]
        nr, nc = r + dr, c + dc
            
        if 0 <= nr < n and 0 <= nc <= nr and tri[nr][nc] == 0:
            tri[nr][nc] = counter
            counter += 1
            r, c = nr, nc
            
        else:
            dir = (dir + 1) % 3
            continue
                
        
    for line in tri:
        answer.extend(line)
    
    return answer