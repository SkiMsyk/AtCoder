n,m = map(int,input().split())
min_value = 1
max_value = n
for _ in range(m):
    l, r = map(int, input().split())
    min_value = max(min_value, l)
    max_value = min(max_value, r)

if min_value > max_value:
    ans = 0
else:
    ans = max_value - min_value + 1
print(ans)