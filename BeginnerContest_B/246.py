# libraries
import math
import numpy as np

# input
a, b = map(int, input().split())
v = np.array([a,b])

# solution
# divide the vector by its abs-norm.
std_v = v / np.sqrt(a*a + b*b)

# normalize
print(' '.join(str(e) for e in std_v))