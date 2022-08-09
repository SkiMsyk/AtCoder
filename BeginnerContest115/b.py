n = int(input())
p = []
for i in range(n):
    p.append(int(input()))

res = sum(p) - int(max(p)/2)
print(res)