r, D, x = map(int, input().split())
def f(x, r = r, D = D):
    return r*x - D
for i in range(10):
    x = f(x)
    print(x)