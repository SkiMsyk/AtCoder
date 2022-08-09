K = int(input())
if K % 2 == 0:
    res = (K/2)**2
else:
    res = ((K-1)/2)*((K-1)/2 + 1)
print(int(res))