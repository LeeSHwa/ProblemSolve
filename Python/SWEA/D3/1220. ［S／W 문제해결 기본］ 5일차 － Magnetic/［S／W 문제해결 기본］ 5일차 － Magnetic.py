T = 10

for tc in range(1, T + 1):
    _ = int(input())
    grid = [list(map(int, input().split())) for _ in range(100)]
    cnt = 0
    
    for col in range(100): # 전치 및 0 제거, 전치하면 왼쪽이 1, 오른쪽이 2
        line = [grid[x][col] for x in range(100) if grid[x][col] != 0]
        length = len(line)
        
        # -> 방향 탐색, 1을 발견하기 전까지 모두 다 1로 바꿔버림 (2가 사라지는 효과)
        for idx in range(length):
            if line[idx] != 1:
                line[idx] = 1
            else:
                break
                
        # <- 방향 탐색, 2를 발견하기 전까지 모두 다 2로 바꿔버림 (1이 사라지는 효과)
        for idx in range(length -1, -1, -1):
            if line[idx] != 2:
                line[idx] = 2
            else:
                break
        

        # 1->2순서로 바뀌는 엣지만 카운팅 (교착상태)
        prev = line[0]
        for idx in range(1, length):
            if prev == 1 and line[idx] == 2:
                cnt += 1
            prev = line[idx]
            
    print(f'#{tc} {cnt}')