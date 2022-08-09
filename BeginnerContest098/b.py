n = int(input())
s= list(input())

res = 0
for i in range(2,n-1):
    res = max(res, len(set(s[:i])&set(s[i:])))

print(res)
