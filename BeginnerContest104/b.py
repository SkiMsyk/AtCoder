s = list(input())

def conditionA(s_list):
    return s[0] == "A"

def conditionC(s_list):
    return "C" in s_list[2:-1]

def conditionLower(s_list):
    return sum([e.isupper() for e in s_list]) == 2

if conditionA(s) and conditionC(s) and conditionLower(s):
    print("AC")
else:
    print("WA")