V,T,S,D = map(int, input().split())
transparency_100_range = [V*T, V*S]
if  (V*T <= D) and (D <= V*S):
    print("No")
else:
    print("Yes")