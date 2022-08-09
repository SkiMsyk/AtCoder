import numpy as np

n = int(input())
v = np.array(list(map(int,input().split())))

# import ipdb; ipdb.set_trace()

if np.unique(v).size == 1:
    print(int(n/2))
else:
    # 偶数要素と奇数要素に分ける
    vo = v[::2]
    ve = v[1::2]
    # それぞれについて最大数の要素を見つける
    vof = np.bincount(vo).argmax()
    vef = np.bincount(ve).argmax()

    if vof == vef:
        if sum(vo == vof) > sum(ve == vef):
            vef = np.bincount(ve[ve!=vef]).argmax()
        elif sum(ve == vef) > sum(vo == vof):
            vof = np.bincount(vo[vo!=vof]).argmax()
        else :
            vof2 = np.bincount(vo[vo!=vof]).argmax()
            vef2 = np.bincount(ve[ve!=vef]).argmax()
            if (sum(vo == vof) + sum(ve == vef2)) > (sum(ve == vef) + sum(vo == vof2)):
                vef = vef2
            else:
                vof = vof2
    
    # それぞれについて最大数の数では無い要素数を数える
    vonf = sum(vo != vof)
    venf = sum(ve != vef)
    # 足しあげる
    print(vonf+venf)