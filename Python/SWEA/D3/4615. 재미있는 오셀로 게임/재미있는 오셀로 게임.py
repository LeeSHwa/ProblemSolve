T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())
    grid = [[0] * n for _ in range(n)]
    grid[n // 2 - 1][n // 2 - 1] = 2
    grid[n // 2 - 1][n // 2] = 1
    grid[n // 2][n // 2 - 1] = 1
    grid[n // 2][n // 2] = 2

    comm = [list(map(int, input().split())) for _ in range(m)]
    
    def check_dir(row, col):
        dirs = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
        can_go = []
        c = grid[row][col]
        for dr, dc in dirs:
            nr, nc = row + dr, col + dc
            if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 3 - c: # 처음 만나는 돌이 기준점의 돌과 다를 때
                nr += dr
                nc += dc
                    
                while 0 <= nr < n and 0 <= nc < n:
                    if grid[nr][nc] == c:
                        can_go.append((dr, dc))
                        break
                    elif grid[nr][nc] == 0:
                        break
                    nr += dr
                    nc += dc
        return can_go
    
    def fill_grid(row, col, dr, dc, c): # (row, col)에서 (dr, dc)방향으로 c를 칠함
        nr, nc= row + dr, col + dc
        
        while 0 <= nr < n and 0 <= nc < n and grid[nr][nc] != c:
            grid[nr][nc] = c
            nr += dr
            nc += dc
	
    for col, row, c in comm:
        grid[row - 1][col - 1] = c
        
        for dr, dc in check_dir(row - 1, col - 1):
            fill_grid(row - 1, col - 1, dr, dc, c)
	
    c1, c2 = 0, 0
    for line in grid:
        for col in line:
            if col == 1:
                c1 +=1
            elif col == 2:
                c2 += 1
    print(f'#{tc} {c1} {c2}')
			