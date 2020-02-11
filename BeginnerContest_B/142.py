# Roller Coaster

# input
N, K = map(int, input().split())
h = list(map(int, input().split()))

# solve
res = sum([hi >= K for hi in h])

# output
print(res)
