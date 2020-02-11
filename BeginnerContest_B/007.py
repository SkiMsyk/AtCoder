from string import ascii_lowercase as alp
A = input()
if len(A) == 1:
    if A == 'a':
        print(-1)
    else:
        print('a')
else:
    print(A[:-1])