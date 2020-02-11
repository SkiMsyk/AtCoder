n = input()
sn = [int(e) for e in list(n)]
n = int(n)

if n % sum(sn) == 0:
    print("Yes")
else:
    print("No")