s = list(input())
k = int(input())

full_list = []

for i in range(len(s)):
    for j in range(i, i+5):
        full_list += [''.join(s[i:j+1])]
        
full_list = list(set(full_list))
full_list.sort()
# print(full_list)
# ここまでで列挙は完了
# 辞書順って先頭，aの方が大きいってことなのね．
print(full_list[k-1])