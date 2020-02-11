s = input()
k = int(input())
cand_list = []
for i in range(len(s)-k+1):
    cand = s[i:i+k]
    if cand not in cand_list:
        cand_list.append(cand)
print(len(cand_list))
