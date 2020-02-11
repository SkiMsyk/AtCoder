# Strings with the Same Length

# input
N = int(input())
S, T = input().split()

# solve
res = ''.join([i+j for i, j in zip(S, T)])

# output
print(res)
