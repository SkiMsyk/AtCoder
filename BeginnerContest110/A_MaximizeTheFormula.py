a,b,c=input().split()
res =  max([int(a+b)+int(c), int(b+a)+int(c),int(a+c)+int(b), int(c+a)+int(b), int(b+c)+int(a), int(c+b)+int(a)])
print(res)