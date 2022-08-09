X = int(input())
if X >= 90:
    print('expert')
else:
    diff = [max(0, e-X) for e in [40, 70, 90, 100]]
    ans = min([e for e in diff if e > 0 ])
    print(ans)
