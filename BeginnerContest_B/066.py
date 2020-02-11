# ss
def is_evenstring(s):
    if s[:len(s)//2] == s[len(s)//2:]:
        return True
    else:
        return False

# input
S = input()

# test
while True:
    S = S[0:-1]
    if is_evenstring(S):
        res = len(S)
        break

print(res)