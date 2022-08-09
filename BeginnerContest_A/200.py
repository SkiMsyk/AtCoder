N = int(input())
x = 1
seiki = 1
while x + 99 <= 3000:
    if (x <= N) and (N <= x + 99):
        ans = seiki
        break
    else:
        x += 100
        seiki += 1
print(ans)