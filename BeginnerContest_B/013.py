a = int(input())
b = int(input())
n1 = a
n2 = a
res = 0
while n1 != b and n2 != b:
    n1 = (n1 - 1) % 10
    n2 = (n2 + 1) % 10
    res += 1
print(res)
