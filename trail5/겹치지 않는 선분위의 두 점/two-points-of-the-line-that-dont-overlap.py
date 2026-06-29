n, m = map(int, input().split())

lines = [tuple(map(int, input().split())) for _ in range(m)]

lines.sort()

left = 0                               # 최소 거리
right = lines[-1][1] - lines[0][0]     # 최대 거리 (마지막 선분의 끝 - 첫 선분의 시작)

answer = 0

while left <= right:
    mid = (left + right) // 2
    
    prev = lines[0][0]
    prev_idx = 0
    flag = False
    
    cnt = 1                             # 첫 점을 안고를 이유가 없음
        
    while prev_idx < m:
        if lines[prev_idx][0] <= prev + mid <= lines[prev_idx][1]:
            prev += mid
            cnt += 1

        elif prev + mid > lines[prev_idx][1]:          
            prev_idx += 1
           
        else:
            prev = lines[prev_idx][0]
            cnt += 1

        if cnt == n:
            flag = True
            break

    if flag:
            left = mid + 1
            answer = mid

    else:
            right = mid - 1

                
print(answer)