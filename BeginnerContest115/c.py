n, k = map(int, input().split())
h = [int(input()) for _ in range(n)]
h.sort()
res = [h[i+k-1]-h[i] for i in range(n-k+1) ]
print(min(res))


# 全ての木小さい順に並べて，端から順にk個選ぶことを順番にやっていくと n-k+1 通りで終わる
