a,b,x = map(int, input().split())
if x < a+b and x >= a:
    print('YES')
else:
    print('NO')