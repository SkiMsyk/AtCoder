N = input()
flag = 0
for i in range(3):
    if N[i] == N[i+1]:
        flag += 1
    if flag != 0 and N[i] != N[i+1]:
        break

if flag >= 2:
    print('Yes')
else:
    print('No')