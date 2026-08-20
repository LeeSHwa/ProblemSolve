n = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.

meetings.sort(key = lambda x : x[1])

cnt = 0
pre_end = -1
for start, end in meetings:
    if pre_end < 0:
        pre_end = end
        cnt += 1
        continue
    
    if start >= pre_end:
       cnt += 1
       pre_end = end

print(cnt) 