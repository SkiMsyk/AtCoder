A,B=map(int,input().split())
# How many are there numbers which are less than B and greater than A
ans = max(0, B-A+1)
print(ans)