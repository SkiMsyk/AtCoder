# One Clue

# input
K, X = map(int, input().split())

# solve
s = max(-1000000, X - K)
e = min( 1000000, X + K)
res = ' '.join([str(e) for e in range(s+1, e)])

# output
print(res)