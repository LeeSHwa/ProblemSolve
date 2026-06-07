n = int(input())

# Please write your code here.
'''
15까지 7개
숫자   8개

        15           30 
3 6 9 12  18 21 24 27
 5   10     20    25 
'''
nums = [0, 1, 2, 4, 7, 8, 11, 13, 14]
if n <= 8:
        print(nums[n])
elif n % 8 == 0:
        print(n // 8 * 15 - 15 + nums[8])
else:
        print(n // 8 * 15 + nums[n % 8])