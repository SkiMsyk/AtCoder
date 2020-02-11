S = [int(e) for e in input()]
res = min(sum(S), len(S) - sum(S))
print(res*2)