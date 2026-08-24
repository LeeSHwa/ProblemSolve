n = int(input())
price = list(map(int, input().split()))

# Please write your code here.

'''
가격이 높아지면 거기서 끊기?
섹터별로 나눠야 함
오르다가 떨어지는 구간
아닌가? 오히려 떨어지다 오르는 구간?

9 - 10 (1원 이득) - 2 (확 떨어짐. 이 때 구매해야함)
- 3 (1원 이득, 뒤에가 더 큰가?) - 6(4원 이득)... 보다 크다면 계속 전진
최대 이득값을 더 큰값으로 매 번 갱신해야함

최소값을 저장해야함 (시작점)
'''

max_diff = 0
std_idx = -1

for idx in range(n):
    if std_idx == -1:
        std_idx = idx
    
    if price[idx] > price[std_idx]:
        max_diff = max(max_diff, price[idx] - price[std_idx])
    
    else:
        std_idx = idx


print(max_diff)