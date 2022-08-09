X,Y = map(int,input().split('.'))
X = str(X)
if (0 <= Y) and (Y <= 2):
    print(X + '-')
elif (3 <= Y) and (Y <= 6):
    print(X + '')
elif (7 <= Y) and (Y <= 9):
    print(X + '+')