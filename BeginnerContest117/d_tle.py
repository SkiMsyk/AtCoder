n, k = map(int, input().split())
a = list(map(int, input().split()))

def f(x):
    return sum([e ^ x for e in a])

best = 0
for i in range(k+1):
    fval = f(i)
if best < fval:
        best = fval
        ansi = i

print(i)
print(best)