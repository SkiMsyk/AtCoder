import itertools

N = int(input())
S = [input() for _ in range(N)]

# there are N person
# i-th person"s name is S[i]
# we wanna choice 3 persons under the conditions as follows:
# 1. any name starts "M", "A", "R", "C", or "H".
# 2. There are no two or more person whose name starts same character.

# 名前の最初の文字だけに注目すれば良い．
# それぞれの文字から始まる人が何人いるかは記憶しておく
# あとは掛け算

# 最初の文字だけのやつ
s = [e[0] for e in S]

# 辞書で記録
d = {'M':0, 'A':0, 'R':0, 'C':0, 'H':0}

# 数え上げる
for e in s:
    if e in d.keys():
        d[e] += 1

# ゼロじゃないものから3つ選んで掛け算して何通りあるか調べる
res = 0

print(d)

for e1, e2, e3 in itertools.combinations(d.keys(), 3):
    res += d[e1]*d[e2]*d[e3]

print(res)
