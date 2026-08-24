n = int(input())

# Please write your code here.

'''
2원이 적게 들수록 이득임
2원을 0개부터 쓰는 것 부터 시작하여 가능여부 / 5원의 개수를 저장함
'''

def is_possible(count_2):
    if (n - 2 * count_2) % 5 == 0:
        return True
    else:
        return False

can_divide = n // 2
flag = False

for i in range(can_divide + 1):
    if is_possible(i):
        print(i + (n - 2 * i) // 5)
        flag = True
        break

if not flag:
    print(-1)