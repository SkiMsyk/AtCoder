A, B = [e + 13 if e == 1 else e for e in map(int, input().split())]
if A > B:
    print("Alice")
elif A == B:
    print("Draw")
else:
    print("Bob")
