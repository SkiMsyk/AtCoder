m = int(input())
if m < 100:
    vv= '00'
elif 100 <= m and m < 1000:
    vv = '0' + str(int(m / 100))
elif 1000 <= m and m <= 5000:
    vv = str(int(m / 100))
elif 6000 <= m and m <= 30000:
    vv = str(int(m / 1000) + 50)
elif 35000 <= m and m <= 70000:
    vv = str(int(((m / 1000) - 30)/5 + 80))
elif 70000 <= m:
    vv = '89'

print(vv)