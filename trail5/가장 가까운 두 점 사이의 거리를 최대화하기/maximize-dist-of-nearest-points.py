''' 
n개의 선분 위 한 점씩을 반드시 고르고
그 점들간의 거리가 최대가 되도록
그렇다면 mid는 최대거리라고 잡아두고
left는 1부터시작, right는 최대 - 최소로
'''

n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]
lines.sort()

left = 1
# 정렬을 한다면 어떻게 해야하지?
# 기준을 정해야하는데
# 시작점으로만 정렬을 한다면?
# 겹칠 일은 없다고 했음. 다 포함하는 경우도 없음
# [1, 3] [1, 5]는 없음 [1, 3] [2, 4]는 존재함
# --> left가 크다면 right도 무조건 클 수밖에 없음
right = lines[-1][1] - lines[0][0]
answer = 1

while left <= right:
    mid = (left + right) // 2
    curr = lines[0][0]
    flag = False
    
    for idx in range(n - 1):
        next_val = max(curr + mid, lines[idx + 1][0])

        if next_val <= lines[idx + 1][1]:
            curr = next_val
        
        else:
            flag = True
            break
            
    
    if flag:
        right = mid - 1
    else:
        answer = mid
        left = mid + 1

print(answer)
        
