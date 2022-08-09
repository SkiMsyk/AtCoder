n = int(input())
l = list(map(int, input().split()))

longest = l.pop(l.index(max(l)))
if longest < sum(l):
    print('Yes')
else:
    print('No')
