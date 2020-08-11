# Next Prime
import numpy as np

# input
X = int(input())

# solve
prime = 0
numbers = np.array(list(range(2, 10**5 + 4)))

while prime < X:
    prime = numbers[0]
    numbers = numbers[numbers % prime != 0]

# output
print(prime)