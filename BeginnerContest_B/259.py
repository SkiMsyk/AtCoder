# import math

# a,b,d = map(int, input().split())

# # なす角を求める
# try:
#     cost = a / (math.sqrt(a**2 + b**2))
#     t = math.acos(cost)
    
#     # ベクトルの長さ
#     r = math.sqrt(a**2 + b**2)

#     # dをラジアンに直して足す
#     dr = math.radians(d)
#     t2 = t + dr

#     # r sin theta', r cos theta' を求める
#     a2 = r*math.cos(t2)
#     b2 = r*math.sin(t2)

# except ZeroDivisionError as e:
#     a2 = 0
#     b2 = 0
    
# finally:    
#     # answer
#     print(a2, b2)


# 回転行列でOK
from math import sin, cos, radians

a, b, d = map(int, input().split())
d = radians(d)
print(a * cos(d) - b * sin(d), a * sin(d) + b * cos(d))
