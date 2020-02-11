# input
A, B, C, D = map(int, input().split())

# processing
# 0 -- A -- B ---...
# 0 ---- C ---- D ---...
res = max(min(B, D) - max(A, C), 0)

# output
print(res)