n = int(input())
res = 0
ok_list = [1,3,7,9]
for a in list(map(int, input().split())):
    if a not in ok_list:
        res += min([a-e for e in ok_list if e < a])
print(res)
