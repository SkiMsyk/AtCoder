N = int(input())
s = sum([1 if _ == 'R' else 0 for _ in input()])
if s > (N - s):
    print('Yes')
else:
    print('No')
