n = int(input())

cards = [True] * (2*n  + 1) # A가 가지고 있는 카드는 True

for _ in range(n):
    cards[int(input())] = False 
'''
1 ~ 2N까지 적힌 카드를 
N장씩 나눠가짐
B가 내는 카드보다 조금 더 큰, 최소차이로 카드를 내야함
하지만 내가 가지고 있는 카드를 먼저 추산해야하나?
결국 sorting해서 인덱스로 접근하면? 
'''

'''
순회하는 과정에서 만약 카드가 False가 나오면 기회를 1개씩 누적시킴
그러던 중 True가 나오면 기회를 소진하며 점수를 1씩 높이면?
'''

b_smaller_candidate = 0
score = 0

for i in range(1, 2 * n + 1):
    if cards[i] and b_smaller_candidate > 0:
        b_smaller_candidate -= 1
        score += 1
    elif cards[i] == False:
        b_smaller_candidate += 1

print(score)
        

    