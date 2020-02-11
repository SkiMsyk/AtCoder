# input
h,w = map(int, input().split())
grid = list()
for _ in range(h):
    grid.append(list(input()))

sharp_ind = set()
count = 0
for i in range(h):
    for j in range(w):
        if grid[i][j] == "#":
            sharp_ind.add((i,j))
            count += 1

check_ind = [(-1,0),(1,0),(0,-1),(0,1)]
check_res = []

for i in range(h):
    for j in range(w):
        if grid[i][j] == '#':
            flag = False
            for r,c in check_ind:
                if (i+r, j+c) in sharp_ind:
                    flag = True
            check_res.append(flag)

if sum(check_res) == count:
    print("Yes")
else:
    print("No")