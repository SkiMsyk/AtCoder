# Some Sums
# input
N, A, B = map(int, input().split())

# solution
res = sum([n for n, y in zip(range(1, N+1), [sum([int(e) for e in str(x)]) for x in range(1, N+1)]) if y >= A and y <= B])

# output
print(res)