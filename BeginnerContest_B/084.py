# Postal Code
# input
A, B = map(int, input().split())
S = input()

# solution
res = 'Yes'
for i in range(len(S)):
    if i == A:
        if S[i] != '-':
            res = 'No'
            break
    else:
        if S[i] not in '0123456789':
            res = 'No'
            break

# output
print(res)

