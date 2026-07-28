'''
3
1 3 6
3 2 2

1.0000
'''

n = int(input())
pos = list(map(int, input().split()))
vel = list(map(int, input().split()))

left = 0
right = 10 ** 9
previous = 0 # 소수점 연산, 10^-5보다 차이가 작다면 round처리 후 종료하기 위함
answer = 0

while True:
    
    mid = (left + right) / 2
    
    max_x1, min_x2 = -1, float('inf')
    
    for i in range(n):
        x1, x2 = pos[i] - vel[i] * mid, pos[i] + vel[i] * mid
        
        max_x1 = max(max_x1, x1)
        min_x2 = min(min_x2, x2)
    
    if max_x1 <= min_x2:
        right = mid
        answer = mid
        
        if abs(answer - previous) < 10 ** -5:
            break
            
    else:
        left = mid    
    
    previous = answer
    
print(f"{answer:.4f}")