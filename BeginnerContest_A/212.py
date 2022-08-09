A,B = map(int,input().split())
res = A+B
if res == A:
    print('Gold')
elif res == B:
    print('Silver')
else:
    print('Alloy')