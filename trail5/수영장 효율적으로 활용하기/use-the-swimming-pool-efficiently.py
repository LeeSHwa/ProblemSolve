n, m = map(int, input().split())
ts = list(map(int, input().split()))

left = ts[0]
right = sum(ts)

answer = 0
max_t = max(ts)

while left <= right:
    mid = (left + right) // 2 # 최대 이용시간
    
    if mid < max_t:
        left = mid + 1
        continue
    
    # rail = 1
    # time = ts[0]

    rail = [0] * m
    rail[0] = ts[0]
    idx = 0
    flag = False

    for i in range(1, n):
        if rail[idx] + ts[i] <= mid:
            rail[idx] += ts[i] 

        else:
            if idx < m - 1:
                idx += 1
                rail[idx] = ts[i]

            else:    
                flag = True # time + t가 mid보다 작으면서 rail을 모두 사용할 때
                break
                
    if flag:
        left = mid + 1
    else:
        right = mid - 1
        answer = mid

print(answer)