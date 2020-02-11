# Collatz Problem
def f(n):
    if n % 2 == 0: return n/2
    else: return 3*n + 1

n = int(input())
past_values = []
iter = 1
while n not in past_values:
    past_values.append(n)
    n = f(n)
    iter += 1

print(iter)
    
