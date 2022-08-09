#----
# Recursive function
def my_factorial(n):
    if n == 0 : return 1
    return n*my_factorial(n-1)

# ok
#----

#----
# fibonach sequence
def fib(n):
    # 1以上のnに対して nを返す
    if n <= 1: return n
    # fib(n-1) + fib(n-2)を返す
    return fib(n-1) + fib(n-2)

# ok 
#----

#----
def fib2(n, memo):
    if n <= 1:
        return n
    if memo[n] != 0:
        return memo[n]
    else:
        memo[n] = fib(n-1) + fib(n-2)
        return memo[n]

def fib_fast(n):
    memo = [0] * (n+1)
    return fib2(n, memo=memo)

# ok
#----
