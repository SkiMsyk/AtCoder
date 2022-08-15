N, M = map(int, input().split())

# 1,2,...,M
# という数列からN個の数字を左から選ぶ組み合わせを列挙することといえる
iter_max = 2**M - 1
pad_n = len(bin(iter_max)[2:])
base_seq = list(range(1, M+1))

for i in range(iter_max, 0, -1):
    b = bin(i)[2:].zfill(pad_n)
    n = sum([ int(e) for e in b ])
    if n == N:
        print(' '.join([ str(e[0]) for e in zip(base_seq, list(b)) if e[1] == '1']))
