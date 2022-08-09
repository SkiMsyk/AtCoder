n = int(input())
cake = 4
donut = 7

if n < 4:
    print("No")
elif n % cake == 0:
    print("Yes")
elif n % donut == 0:
    print("Yes")
else:
    max_cake = n % cake
    flag = False
    for n_cake in range(1,max_cake+1):
        # import ipdb; ipdb.set_trace()
        if ((n - (n_cake * cake)) % donut) == 0:
            flag = True
            break
    if flag:
        print("Yes")
    else:
        print("No")