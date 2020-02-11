N = int(input())
A = [e for e in list(map(int, input().split())) if e != 0]
res = sum(A)/len(A)
if res - int(res) == 0:
    print(int(res))
else:
    print(int(res)+1)
