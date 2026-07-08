'''
입력
5
0 0 0 3 3
0 0 0 0 3
0 9 9 3 3
9 9 9 3 3
9 9 9 9 3
'''
from collections import deque

n = int(input())

grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
HALF = n**2 // 2 if n % 2 == 0 else n ** 2 // 2 + 1

answer = None

def search(row, col, d):
    
    dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    q = deque()
    
    q.append((row, col))
    visited[row][col] = True
    count = 1
    
    while q:
        r, c = q.popleft()
        
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and abs(grid[nr][nc] - grid[r][c]) <= d:
                q.append((nr, nc))
                visited[nr][nc] = True        
                count += 1
                    
        if count >= HALF:
            return True 
            
    return False
    

left = 0
right = 1000000

while left <= right:
    mid = (left + right) // 2
    flag = False
    
    visited = [[False] * n for _ in range(n)]    
    
    for row in range(n):
        if flag: break
        
        for col in range(n):
            if not flag and not visited[row][col] and search(row, col, mid):
                flag = True
                break
    if flag:
        right = mid - 1
        answer = mid
    else:
        left = mid + 1                        

print(answer)