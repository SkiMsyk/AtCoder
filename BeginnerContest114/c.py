#----------------
# 入力パート
s = input()
#----------------

#----------------
# 列挙パート
all_list = []

# 3桁未満はありえないので3桁の数を列挙
for i in '753':
    for j in '753':
        for k in '753':
            all_list.append(''.join([i,j,k]))

# 与えられた数字の桁数まで，既に列挙してあるものの先頭に7,5,3を付け足していく
for i in range(4,len(s)+1):
    add_list = []
    for c in '753':
        add_list += [''.join(c+e) for e in all_list]
    all_list += add_list

# 重複を排除する
all_list = set(all_list)
#----------------

#----------------
# 回答パート 
# 各要素を集合に変換して{'7','5','3'}と同じになり，かつ与えられた数以下であるかを判定し合計する
res = sum([True for _ in all_list if set(list(_))=={'7','5','3'} and int(_) <= int(s)])
print(res)
#----------------
