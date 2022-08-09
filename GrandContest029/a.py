# N 個のオセロの石が一列に並んでいます。
# それぞれの石の状態は長さ N の文字列 S によって表されており、
#  Si=B のとき左から i 番目の石の表面は黒色、 
#  Si=W のとき左から i 番目の石の表面は白色となっています。

# ここで、以下の操作を行うことを考えます。

# 左から i 番目の石の表面が黒色、左から i+1 番目の石の表面が白色であるような i (1≤i<N) を一つ選び、 
# その 2 つの石をともに裏返す。
# つまり、左から i 番目の石の表面が白色、左から i+1 番目の石の表面が黒色になるようにする。
# 最大で何回この操作を行うことができるか求めてください。

# 制約
# 1≤|S|≤2×105
# Si=B または W

#----
# とりあえず見つけたらやる方式

s = list(input())
count = 0
iter_first = 0
iter_flag = True
for i in range(iter_first, len(s)-1):
    if s[i]+s[i+1] == "BW":
        s[i] = "W"
        s[i+1] = "B"
        count += 1
        bn = 1
        print(s)
        while i > 0 and s[i-bn] + s[i-(bn-1)] == "BW":
            s[i-bn] = "W"
            s[i-(bn-1)] = "B"
            bn + 1
            count += 1
            print(s)
print(count)