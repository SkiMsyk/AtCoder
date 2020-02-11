X, Y = input().split()
d = {'A':1, 'B':2, 'C':3,
    'D':4, 'E':5, 'F':6}

if d[X] < d[Y]:
    print('<')
elif d[X] == d[Y]:
    print('=')
else:
    print('>')
