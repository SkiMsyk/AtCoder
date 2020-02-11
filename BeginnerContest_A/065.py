X, A, B = map(int, input().split())

if 0 < B - A and B - A <= X:
    print("safe")
elif B - A <= 0 and B - A <= X:
    print("delicious")
else:
    print("dangerous")