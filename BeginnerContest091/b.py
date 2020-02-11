# n blue card
n = int(input())
s = [input() for _ in range(n)]

# m red card
m = int(input())
t = [input() for _ in range(m)]

best = -200

for w in set(s + t):
    r = sum([1 for _ in s if _ == w]) - sum([1 for _ in t if _ == w])
    if r > best:
        best = r

if best < 0:
    best = 0
    
print(best)
