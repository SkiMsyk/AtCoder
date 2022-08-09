N = int(input())
L = list(map(int,input().split()))

# Conditions of making triangle
## sum of any two edges l1, l2 is greater than equal other edge l3
## therefore l1 + l2 > l3
ans = 0
for i in range(N):
    for j in range(N):
        for k in range(N):
            if (i < j) and (j < k):
                l = sorted([L[i], L[j], L[k]])
                if (l[2] < l[0] + l[1]) and (L[i] != L[j]) and (L[j] != L[k]) and (L[k] != L[i]):
                    ans += 1
print(ans)