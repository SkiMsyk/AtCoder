# Achieve the Goall
N, K, M = map(int, input().split())
A = sum(list(map(int, input().split())))
An = N*M - A
print([-1, max(0, An)][An <= K])