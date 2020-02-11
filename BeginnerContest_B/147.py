# Palindrome-philia

# input
S = input()

# solve
if len(S) % 2 != 0:
    S = S[:len(S)//2] + S[len(S)//2 + 1:]

res = sum([i != j for i, j in zip(S[:len(S)//2], S[len(S)//2:][-1::-1])])

# output
print(res)