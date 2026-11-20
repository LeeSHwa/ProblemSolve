T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    
    nums = set()
    k = 1
    while len(nums) < 10:
        
        str_n = list(map(int, str(n * k)))
        for num in str_n:
            nums.add(num)
        k += 1
    
    print(f'#{tc} {(k - 1) * n}')