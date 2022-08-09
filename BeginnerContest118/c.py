N = int(input())
A = sorted(list(map(int, input().split())))

# 最大公約数を求める関数
def gcd(a,b):
    rem = a % b
    while rem != 0:
        a = b
        b = rem
        rem = a % b
    return b

cand = A[0]

for i in range(1,N):
    cand = gcd(cand, A[i])

    if cand == 1:
        break

print(cand)