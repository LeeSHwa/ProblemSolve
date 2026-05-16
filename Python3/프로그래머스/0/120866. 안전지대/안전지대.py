def solution(board):
    answer = 0
    length = len(board)
    visited = [[False] * length for _ in range(length)]
    
    def boom(row, col):
        
        visited[row][col] = True
        
        for dr, dc in [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]:
            nr = row + dr
            nc = col + dc
            
            if 0 <= nr < length and 0 <= nc < length and board[nr][nc] != 1 and not visited[nr][nc]:
                visited[nr][nc] = True
    
    
    for row in range(length):
        for col in range(length):
            if board[row][col] == 1 and not visited[row][col]:
                boom(row, col)
    
    for row in range(length):
        for col in range(length):
            if visited[row][col] == False:
                answer += 1
                
    return answer