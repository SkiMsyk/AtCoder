# Airplane
# input
P, Q, R = map(int, input().split())

# solution
res = min(P+Q, P+R, Q+R)

# output
print(res)