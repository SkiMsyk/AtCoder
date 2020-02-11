S = input()
K = int(input())
s_list = list(map(int, list(S)))

flag = False
for k in range( min(len(S), K) ):
    if s_list[k] != 1:
        flag = True
        break

if flag:
    print(s_list[k])
else:
    print(1)