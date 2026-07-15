'''
입력
3 5
20 21 18 99 5
19 22 20 16 26
18 17 40 60 80
1 0 0 0 1
0 0 0 0 0
0 0 0 0 1

출력
21
'''
from collections import deque

m, n = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(m)]
colored = []

for row in range(m):
    line = list(map(int, input().split()))
    for col in range(n):
        if line[col] == 1:
            colored.append((row, col))
    
left = 0
right = 10**9

answer = 0

while left <= right:
    mid = (left + right) // 2
    
    flag = False
    visited = [[False] * n for _ in range(m)]
    q = deque()
    
    start_r, start_c = colored[0][0], colored[0][1]
    
    q.append((start_r, start_c))
    visited[start_r][start_c] = True
    
    while q:
        r, c = q.popleft()
        
        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc] and abs(grid[r][c] - grid[nr][nc]) <= mid:
                q.append((nr, nc))
                visited[nr][nc] = True
    
    for row, col in colored:
        if not visited[row][col]:
            flag = True
            break
    
    if flag:
        left = mid + 1
    else:
        right = mid - 1
        answer = mid

print(answer)