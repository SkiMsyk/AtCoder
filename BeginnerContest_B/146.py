# ROT N

# libraries
from string import ascii_uppercase as ALP

# input
N = int(input())
S = input()

# solve
ALPALP = ALP + ALP

def f(s, N = N):
    return ALPALP[ALPALP.index(s) + N]

res = ''.join([f(s) for s in S])

# output
print(res)