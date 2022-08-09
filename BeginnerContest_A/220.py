A,B,C = map(int,input().split())
cand = ((A // C) + (A % C != 0)) * C
if (A <= cand) and (cand <= B):
    print(cand)
else:
    print(-1)