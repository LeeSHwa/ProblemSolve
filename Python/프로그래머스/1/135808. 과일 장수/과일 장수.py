def solution(k, m, score):
    
    len_score = len(score)
    
    # 예외처리
    if m > len_score:
        return 0
    
    answer = 0
    
    score.sort(reverse=True)
    
    for i in range(m - 1, len_score, m):
        answer += score[i] * m
    
    return answer