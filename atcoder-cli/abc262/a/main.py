Y = int(input())
y = Y - 2
if y % 4 == 0:
    ans = Y
else:
    ans = Y + (4 - y % 4) 
print(ans)
