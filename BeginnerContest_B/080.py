# input()
N = int(input())

# solution
fx = sum([int(e) for e in str(N)])
if N % fx == 0:
    res = 'Yes'
else:
    res = 'No'

# output
print(res)