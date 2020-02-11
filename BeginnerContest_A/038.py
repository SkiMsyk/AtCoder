S = input()

def answer(test):
    if test:
        return "YES"
    else:
        return "NO"

print(answer(S[-1] == "T"))