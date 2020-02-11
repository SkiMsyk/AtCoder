a, b = [True if e == "H" else False for e in input().split()]
if a and b:
    print("H")
elif not a and not b:
    print("H")
else:
    print("D")
