def solution(cost, hint):
    answer = float('inf')
    extra = 0

    n = len(cost)
    k = len(hint[0]) - 1

    arr = [0] * n # [0, 1, 1, 0, 0]

    def sum_cost(arr):
        sum_of_cost = 0
        
        for i in range(n):
            col = arr[i] if arr[i] < n - 1 else n - 1
        
            sum_of_cost += cost[i][col]
        
        return sum_of_cost

    def backtrack(discount_idx):
        nonlocal answer, extra

        # 1. 종료조건
        if discount_idx == n - 1:
            answer = min(answer, sum_cost(arr) + extra)
            return
        
        # 2. append, 추가하는 과정(positive)
        extra += hint[discount_idx][0]
        for i in range(1, k + 1): # 1, 2, ... , k-1
            arr[hint[discount_idx][i] - 1] += 1
                
        # 3. 한층 더 깊게 들어가기
        backtrack(discount_idx + 1)

        # 4.되돌리기
        extra -= hint[discount_idx][0]
        for i in range(1, k + 1): # 1, 2, ... , k-1
            arr[hint[discount_idx][i] - 1] -= 1
        
        # 5. 한층 더 깊게 들어가기
        backtrack(discount_idx + 1)


    backtrack(0)
    return answer