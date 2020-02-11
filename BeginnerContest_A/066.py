bells = list(map(int, input().split()))
print(sum(bells) - bells[bells.index(max(bells))])
