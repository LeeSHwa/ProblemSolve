T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    
    cols = [-1] * n
    answer = 0
    
    def backtrack(depth):
        global answer
        
        if depth == n:
            answer += 1

            return
        
        impossible = set()
        
        for col, row in enumerate(cols):
            if row >= 0:

                impossible.add(col - (depth- row))
                impossible.add(col + (depth - row))
                    
       # print(cols, depth, impossible)
        
        for i in range(n):
            if cols[i] == -1 and i not in impossible:
                cols[i] = depth

                backtrack(depth + 1)

                cols[i] = -1
    
    backtrack(0)
    print(f'#{tc} {answer}')