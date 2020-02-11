# Greedy Takahashi

# input
A, B, K = map(int, input().split())

# solve
resA = max(0, A - K)
resB = max(0, B - max(0, K - A))

# output
print(resA, resB)