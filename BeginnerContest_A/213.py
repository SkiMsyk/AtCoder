A,B=map(int,input().split())
ans = bin(A ^ B) 
print(int(ans, 2))