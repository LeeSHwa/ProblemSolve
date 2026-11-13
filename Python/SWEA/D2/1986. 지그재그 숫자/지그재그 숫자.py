T = int(input())
'''
1 2 3 4 5 6 7 8
0 1 2 3 4 5 6 7
1 + 3 + 5
- ( 2 + 4 + 6 )
idx 2마다 -1이 쌓이며 idx가 홀수라면 홀수 idx가 정답이 됨
'''
for tc in range(1, T + 1):
    n = int(input())
    print(f'#{tc}', end = " ")
    if n == 1: 
        print(1)
    elif n % 2 == 0:
        print(- (n // 2))
    else:
        print((n + 1) // 2)