n = int(input())
d = {}
a = list(map(int, input().split()))
ans = 'YES'
for ai in a:
    if ai not in d.keys():
        d[ai] = 1
    else:
        ans = 'NO'
        break
print(ans)