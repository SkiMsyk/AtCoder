# input
N = int(input())
K = int(input())

# processing
## definition of function
def opeA(num):
    return num*2

def opeB(num, K = K):
    return num + K

## initial
num = 1

for i in range(N):
    if opeA(num) < opeB(num):
        num = opeA(num)
    else:
        num = opeB(num)

# output
print(num)