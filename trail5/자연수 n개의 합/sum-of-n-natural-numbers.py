s = int(input())

def para(target):
    left = 1
    right = int(2 * target ** 0.5)

    max_n = -1

    while left <= right:
        mid = (left + right) // 2

        if mid * (mid + 1) // 2 <= target:
            left = mid + 1
            max_n = max(max_n, mid)
        else:
            right = mid - 1

    return max_n

print(para(s))