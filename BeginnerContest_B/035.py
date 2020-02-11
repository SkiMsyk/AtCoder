S = input()
T = input()
L = S.count('L')
R = S.count('R')
U = S.count('U')
D = S.count('D')
q_count = S.count('?')

if T == '2':
        res = max(len(S) % 2, abs(L-R) + abs(U-D)-q_count)
else:
    res = abs(L - R) + abs(U - D) + q_count

print(res)