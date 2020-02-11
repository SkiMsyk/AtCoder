# input
N = int(input())

# solution
prev = [2, 1]
if N == 1:
    res = 1
else:
    for i in range(2, N+1):
        prev[0], prev[1] = prev[1], sum(prev)
    res = prev[1]

# output
print(res)