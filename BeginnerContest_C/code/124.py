s = input()
cand = [0, 0]
pat1 = ''
pat2 = ''
# index 0 は 0始まり
# index 1 は 1始まり
for i, si in enumerate(s):
    si = int(si)
    if i % 2 == 0:
        # 偶数の時
        cand[0] += si != 0
        cand[1] += si != 1
        
        pat1 += '0'
        pat2 += '1'
    else:
        # 奇数の時
        cand[0] += si != 1
        cand[1] += si != 0
        
        pat1 += '1'
        pat2 += '0'
    
print(min(cand))    
