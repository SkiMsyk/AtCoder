N = int(input())
ans = 0

if N >= 10**3:
    ans += min(N, 999_999) - 999

if N >= 10**6:
    ans += (min(N, 999_999_999) - 999_999) * 2 

if N >= 10**9:
    ans += (min(N, 999_999_999_999) - 999_999_999) * 3

if N >= 10**12:
    ans += (min(N, 999_999_999_999_999) - 999_999_999_999) * 4

if N == 10 ** 15:
    ans += 5

print(ans)
