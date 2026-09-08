n = int(input())
nums = [tuple(map(int, input().split())) for _ in range(n)]

nums.sort(key = lambda x : x[1])
# Please write your code here.


'''
상태기계 설계?

-----------------
->             <-
이 방향으로 진행을 하며, 대상이 되는 두 수의 개수를 기준으로
더 작은 값만큼 더하고, 개수가 0이 되면 다음 값으로 이동
더 큰 값은 해당하는 작은값만큼 빼고 갱신
이렇게 리스트를 만들어(heap에 넣는게 더 이득일 것 같긴 하지만) 가능한 모든 합을 구하고
그 중 최소값을 구하기
'''

left = 0
right = n - 1

left_count = nums[left][0]
right_count = nums[right][0]

sums = []

while left < right:
    sums.append(nums[left][1] + nums[right][1])

    if left_count > right_count:
        left_count -= right_count
        right -= 1
        right_count = nums[right][0]

    elif right_count > left_count:
        right_count -= left_count
        left += 1
        left_count = nums[left][0]
    
    else:
        left += 1
        right -= 1
        right_count = nums[right][0]
        left_count = nums[left][0]


print(max(sums))