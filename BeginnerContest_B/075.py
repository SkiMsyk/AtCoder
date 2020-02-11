# Minesweeper

# libraries
import itertools

# input
H, W = map(int, input().split())
R = [[0 for i in range(W+2)] for j in range(H+2)]
memo = []

# processing
for h in range(1, H+1):
    for w, s in zip(range(1, W+1), input()):
        if s == '#':
            memo.append([h, w])
            for i, j in itertools.product([-1, 0, 1], [-1, 0, 1]):
                R[h+i][w+j] += 1

for h, w in memo:
    R[h][w] = '#'

# output
for S in R[1:-1]:
    print(''.join([str(e) for e in S[1:-1]]))