# input
N = int(input())

# process
cand = [2**e for e in range(0,7)]
res = max([e for e in cand if N - e >= 0])

# output
print(res)