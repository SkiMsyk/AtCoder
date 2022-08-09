N = int(input())
S = input().split()

# P:peach
# W:white
# G:green
# Y:yellow

# S[i]: color of i-th bean
# 3 color variation in given case -> return "Three"
# 4 color variation in given case -> return "Four"

if len(set(S)) == 3:
    print("Three")
else:
    print("Four")