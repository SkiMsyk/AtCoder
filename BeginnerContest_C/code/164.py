# input
n = int(input())
s = ['']*n
for _ in range(n):
    s[_] = input()
    
print(len(set(s)))
