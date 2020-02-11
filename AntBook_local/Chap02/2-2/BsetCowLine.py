# given s: n-length string
# make t : n-length string too
# first of all, length of t is 0
# then, we can do one of below
#   - omit first string in s and add the string into tail of s
#   - omit last string in s and add the string into head of s
# 
# Q: make t as small as possibly in dictionary order.

# 方針:追加できる２つの文字のうち，辞書順で小さい方を追加する
# ただし，同じ文字の場合はその次の文字を見る必要がある
# そこで，順序を反転させた文字列を用意すれば先読み，後戻りの必要をなくせる

n = 6
s = 'ACDBCB'
t = ''
while s:
    invs = ''.join([s[-1::-1]])
    if s[0] < invs[0]:
        t += s[0]
        s = s[1:]
    else:
        t += invs[0]
        s = s[:-1]
print(t)