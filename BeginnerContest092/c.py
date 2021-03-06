# x 軸上に N 個の観光スポットがあり、1,2,…,N の番号がついています。 
# 観光スポット i は座標 Ai の点にあります。 
# また、x 軸上を座標 a の点から座標 b の点まで移動するには |a−b| 円かかります。

# あなたは x 軸上を旅行する計画を立てました。 
# 計画では、最初に座標 0 の点を出発し、N 個の観光スポットを番号順に訪れ、最後に座標 0 の点に戻ってくることになっています。

# ところが、旅行の直前に急用が入り、N 個すべての観光スポットを訪れる時間的余裕がなくなってしまいました。 
# そこで、ある i を選び、観光スポット i を訪れるのを取りやめることにしました。 
# それ以外の観光スポットは予定通り番号順に訪れます。 
# また、最初に座標 0 の点を出発し、最後に座標 0 の点に戻ってくることについても、予定に変更はありません。

# i=1,2,…,N それぞれについて、観光スポット i を訪れるのを取りやめたときの、旅行中の移動にかかる金額の総和を求めてください。

n = int(input())
a = list(map(int,input().split()))

# 元々の総額を計算する  
orgnl = sum([a[0]] + [abs(s-g) for s,g in zip(a[:n-1], a[1:])] + [a[-1]])

# i番目を抜くというのは orgnl の abs(a[i-1]-a[i]) + abs(a[i]-a[i+1]) を引いて
# abs(a[i-1]-a[i+1])を足すことに等しいので１つ飛ばしの差分を使えば良い
for i in range(n):
    if i == 0:
        print(orgnl - (abs(a[i]) + abs(a[i]-a[i])) + abs(a[i+1]) )
    elif i == n-1:
        print(orgnl - (abs(a[i-1]-a[i])+abs(a[i])) + abs(a[i]))
    else:
        print(orgnl - (abs(a[i-1]-a[i]) + abs(a[i]-a[i+1])) + abs(a[i-1]-a[i+1]))
