# Echo

# input
N = int(input())
S = input()

# solve
if N % 2 != 0:
    res = 'No'
else:
    if S[:len(S)//2] == S[len(S)//2:]:
        res = 'Yes'
    else:
        res = 'No'

# output
print(res)