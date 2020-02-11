n = int(input())
an, an_1 , an_2 = 0,0,1
for _ in range(n-1):
    an, an_1, an_2 = an_1, an_2, (an + an_1 + an_2) % 10007
print(an)