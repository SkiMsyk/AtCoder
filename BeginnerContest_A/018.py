p = []
for i in range(3):
    p.append(int(input()))
sorted_p = sorted(p, reverse = True)
for i in p:
    print(str(sorted_p.index(i)+1))
