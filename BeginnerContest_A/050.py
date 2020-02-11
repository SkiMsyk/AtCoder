A, op, B = [int(e) if e not in {"+", "-"} else e for e in input().split()]
if op == "+":
    print(A + B)
else:
    print(A - B)