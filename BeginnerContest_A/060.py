x = input()
s = [elm[0] for elm in x.split()[1:]]
e = [elm[-1] for elm in x.split()[:-1]]
if s == e:
    print("YES")
else:
    print("NO")
