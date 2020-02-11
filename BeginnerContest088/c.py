import numpy as np

grid = [np.array(list(map(int, input().split()))) for _ in range(3)]

# check bi
aib1 = np.array([e[0] for e in grid])
aib2 = np.array([e[1] for e in grid])
aib3 = np.array([e[2] for e in grid])

if len(set(aib1 - aib2)) == 1 and len(set(aib2 - aib3)) and len(set(aib3 - aib1)) == 1:
    if len(set(grid[0] - grid[1])) == 1 and len(set(grid[1] - grid[2])) == 1 and len(set(grid[2]-grid[0])) == 1:
        print("Yes")
else:
    print("No")