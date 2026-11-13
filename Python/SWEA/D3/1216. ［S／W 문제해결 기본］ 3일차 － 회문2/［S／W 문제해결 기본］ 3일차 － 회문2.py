for _ in range(10):
    tc = int(input())

    grid = [list(input()) for _ in range(100)]

    answer = 1
    dirs = [(1, 0), (0, 1)]
    
    def check(arr):
        length = len(arr)
        for idx in range(length // 2):
            if arr[idx] != arr[-(idx + 1)]:
                return False
        return True
          
    for row in range(100):
        for col in range(100):
            start = grid[row][col]
            
            for dr, dc in dirs:
                nr, nc = row + dr, col + dc
                if dc and 100 - row <= answer:
                    continue
                if dr and 100 - col <= answer:
                    continue
                    
                while nr < 100 and nc < 100:
                    if grid[nr][nc] == start:
                        # 가로의 경우
                        if dc and check(grid[row][col : nc + 1]):
                            answer = max(answer, nc - col + 1)
                        # 세로의 경우
                        elif dr and check([grid[r][col] for r in range(row, nr + 1)]):
                            answer= max(answer, nr - row + 1)
                    nr += dr
                    nc += dc

    print(f'#{tc} {answer}')