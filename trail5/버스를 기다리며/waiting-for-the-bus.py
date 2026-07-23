'''
가장 오래 기다려야 하는 사람이 기다리는 시간의 최소값 
-> 모두를 다 태울 수 있는 최소 타임블럭?
-> 어짜피 모두 태워야 하는거임
-> 정렬해서, 그냥 사람이 있을 때 마다 타임블럭을 씌우고
-> 그 타임블럭 안에 사람이 있다면 가능한 만큼(C만큼) 태우고
-> 더이상 못들어가면 타임블럭의 개수를 하나 늘리기

6 3 2
1 1 10 14 4 3

4
'''
n, m, c = map(int, input().split())
ts = list(map(int, input().split()))

ts.sort()
left = 0
right = ts[-1] - ts[0]

answer = 0

while left <= right:
    mid = (left + right) // 2
    
    last_idx = ts[0] + mid      # 버스가 기다릴 수 있는 끝 시간
    cnt = 1                     # 해당 버스에 몇 명이 탔는지
    bus = 1                     # 버스 개수 ( <= m )
    
    flag = False        # m개의 버스에 다 못태우는 경우
    
    for idx in range(1, n):
        if ts[idx] <= last_idx:
            if cnt < c:
                cnt += 1
                
            else:
                if bus < m:
                    bus += 1
                    cnt = 1
                    last_idx = ts[idx] + mid
                else:
                    flag = True
                    break

        else:
            if bus < m:
                bus += 1
                cnt = 1
                last_idx = ts[idx] + mid
                
            
            else:
                flag = True
                break

    if flag: # 다 못태운다면 => 대기시간이 너무 짧은거 -> 늘려야함
        left = mid + 1
    else:
        right = mid - 1
        answer = mid

print(answer)
            
    