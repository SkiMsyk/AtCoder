n = int(input())
p = list(map(int, input().split()))

minvalue = n+1
ans = 0
for pi in p:
    if minvalue > pi:
        minvalue = pi
        ans += 1

print(ans)