# H and V
# 高々 2 ** 12 通りなので全探索で良い
import numpy as np
H,W,K = map(int,input().split())
HW = np.repeat('', H*W).reshape(H,W) 
ans = 0
for _ in range(H):
    HW[_] = np.array(list(input()))

for _ in range(1<<(H+W)):
    # print(format(_, 'b').zfill(H+W))
    choices = format(_, 'b').zfill(H+W)
    r = [i for i, v in enumerate(choices[:H]) if v == '1']
    c = [i for i, v in enumerate(choices[H:]) if v == '1']
    ans += [0, 1][np.sum(HW[r,:][:,c] == '#') == K]

print(ans)
    
    