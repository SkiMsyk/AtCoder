d, g = map(int, input().split())
ps = list()
cs = list()
completeBonus = list()
for i in range(d):
    p, c = map(int, input().split())
    ps.append(p)
    cs.append(c)
    completeBonus.append(p*(i+1)*100 + c)

# import ipdb; ipdb.set_trace()
res = sum(ps)

# 目標得点と同じ配点の問題があればそれを一問とけば良い
if g in [i*100 for i in range(1,d+1)]:
    print(1)
else:
    # ある問題だけをいくつかとけば良い場合
    for i,p in zip(range(1,len(ps)+1),ps):
        for j in range(1,p+1):
            if g <= i*100*j:
                res = min(res,j)       
    # 問題数が少ないかつ得点が高いかつコンプリートボーナスが高いもの解いていく
    # 解く，解かないの組み合わせ 2**D を総当たりする
    for i in range(1, (1 << d)):
        # import ipdb; ipdb.set_trace()
        completeNumber = format(i, '0'+str(d)+'b')
        basePoint = 0
        problemNumber = 0
        for j in range(d):
            if completeNumber[j] == '1':
                basePoint += completeBonus[j]
                problemNumber += ps[j]

        # まだ得点が足りなかった場合は残っている一番得点の高い問題解いていく
        # 全部解いても得点が足りない場合はカウントしない
        # import ipdb; ipdb.set_trace()
        if basePoint < g:
            for j in range(d,0,-1):
                if completeNumber[j-1] == '0':
                    if abs(basePoint - g) < (j* 100 * (ps[j-1])):
                        # import ipdb; ipdb.set_trace()
                        if (abs(basePoint - g) % (j * (i+1) * 100)) == 0:
                            problemNumber += (abs(basePoint - g) // (j * i * 100))
                        else:
                            problemNumber += (abs(basePoint - g) // (j * i * 100)) + 1
                        res = min(res, problemNumber)
        else:
            res = min(res, problemNumber)

print(res)