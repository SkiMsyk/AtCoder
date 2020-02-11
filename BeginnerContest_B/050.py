# input
N = int(input())
T = list(map(int, input().split()))
M = int(input())
P = list()
X = list()
res = [0]*M

for _ in range(M):
    p, x = map(int, input().split())
    res[_] = sum(T) - (T[p-1] - x)

for e in res:
    print(e)
