def solution(left, right):
    answer = 0
    
    def divide(num):
        cnt = 0
        if num == 1:
            return False
        
        for i in range(2, (num // 2) + 1):
            if num % i == 0:
                cnt += 1
                
        return True if cnt % 2 == 0 else False
    
    for num in range(left, right + 1):
        if divide(num):
            answer  += num
        else:
            answer -= num
        
    
    return answer