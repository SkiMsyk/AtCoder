# input
N = int(input())
K = int(input())
x = list(map(int, input().split()))

# processing
res = sum([min([abs(e - 0), abs(e - K)])*2 for e in x])

# output
print(res)