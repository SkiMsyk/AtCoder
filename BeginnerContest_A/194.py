nonfat, fat = map(int, input().split())
def is_IceCream(nonfat, fat):
    return (nonfat + fat >= 15) and (fat >= 8)

def is_IceMilk(nonfat, fat):
    return (~is_IceCream(nonfat, fat)) and (nonfat + fat >= 10) and (fat >= 3)

def is_LacticIce(nonfat, fat):
    return (~is_IceMilk(nonfat, fat)) and (nonfat + fat >= 3)

def is_FrozenDessert(nonfat,fat):
    return ~is_LacticIce(nonfat, fat)

if is_IceCream(nonfat, fat):
    print(1)
elif is_IceMilk(nonfat, fat):
    print(2)
elif is_LacticIce(nonfat, fat):
    print(3)
elif is_FrozenDessert(nonfat, fat):
    print(4)