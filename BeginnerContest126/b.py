S = input()
mlist = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
if S[0:2] in mlist and S[2:] in mlist:
    print('AMBIGUOUS')
elif S[0:2] in mlist:
    print('MMYY')
elif S[2:] in mlist:
    print('YYMM')
else:
    print('NA')