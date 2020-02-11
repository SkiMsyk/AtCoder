# a,b,c からなる長さ 3 の文字列 S が与えられます。S を abc を並び替えて作ることができるかどうか判定してください。

# 制約
# |S|=3
# S は a,b,c からなる

s = set(list(input()))
if s == {'a','b','c'}:
    print('Yes')
else:
    print('No')
