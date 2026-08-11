'''
3 5
1 4 6 3 5
5 4 3 7 2
7 3 1 5 4

4
'''
from collections import deque

n, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

left = 0
right = 499

def explore(L, R):
    if grid[n - 1][m - 1] > R or grid[n - 1][m - 1] < L:
        return False

    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    
    q = deque()
    q.append((0, 0))
    
    while q:
        r, c = q.popleft()
        
        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and L <= grid[nr][nc] <= R:
                visited[nr][nc] = True
                q.append((nr, nc))
    
    return visited[n-1][m-1]
            

answer = None
            
while left <= right:
    mid = (left + right) // 2
    flag = False
    
    for start in range(max(1, grid[0][0] - mid), grid[0][0] + 1):
        if explore(start, min(start + mid, 500)):
            flag = True
            break
    
    if flag:
        right = mid - 1
        answer = mid
    else:
        left = mid + 1

print(answer)