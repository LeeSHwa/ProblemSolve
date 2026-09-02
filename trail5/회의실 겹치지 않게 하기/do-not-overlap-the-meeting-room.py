n = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.

meetings.sort(key = lambda x : x[1])

prev_start, prev_end = -1, -1
cnt = 0

for start, end in meetings:
    if start >= prev_end:
        prev_start, prev_end = start, end
        cnt += 1

print(n - cnt) 