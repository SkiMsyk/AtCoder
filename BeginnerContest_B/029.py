res = 0
for _ in range(12):
    s = input()
    if s.__contains__('r'):
        res += 1
print(res)
