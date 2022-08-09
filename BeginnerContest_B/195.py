a, b, w = map(int, input().split())
w *= 1000
 
# 整数商が同じの時，割り切れなければWを満たさない
if (w // a == w // b) and (w % a != 0) and (w % b != 0):
    print('UNSATISFIABLE')
else:
    # Wを満たす場合がある
    # 最小値aで割った整数商がrmax
    # 最大値bで割った整数商+1がrmin
    rmax = w // a
    rmin = w // b + [0,1][w % b != 0]
    print(rmin, rmax)
    
    
    
    
    
    