from collections import deque

def solution(ps, loc):
    q = deque(ps)
    
    cnt = 1
    
    while q:
        popped = q.popleft()
        
        flag = False
        
        for p in q:
            if p > popped:
                q.append(popped)
                flag = True
                break
        
        if flag:
            if loc == 0:
                loc = len(q) - 1
            else: 
                loc -= 1
            
            continue
            
        else:
            if loc == 0:
                return cnt
            else:
                cnt += 1
                loc -= 1
        
    