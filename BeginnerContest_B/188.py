n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

res = sum([a*b for a,b in zip(A,B)])
print(['Yes','No'][res!=0])