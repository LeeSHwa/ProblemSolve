from functools import cmp_to_key

n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.

def custom_key(a, b):

    if str(a) + str(b) > str(b) + str(a):
        return -1
    
    elif str(b) + str(a) > str(a) + str(b):
        return 1
    
    else:
        return 0

arr.sort(key = cmp_to_key(custom_key))

for x in arr:
    print(x, end = "")