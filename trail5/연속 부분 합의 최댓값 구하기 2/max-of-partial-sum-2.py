n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
seq_sum = 0
answer = 0

if max(a) < 0:
    print(max(a))
    quit()
for num in a:
    seq_sum += num

    if seq_sum < 0:
        seq_sum = 0
    else:
        answer = max(answer, seq_sum)


print(answer)