N = int(input())
words = []

rule_length = True
rule_2time = True
rule_startEnd = True

for i in range(N):
    word = input()
    if 1 > len(word) or len(word) > 10:
         rule_length = False
    if word in words:
        rule_2time = False
    if i !=0 and words[-1][-1] != word[0]:
        rule_startEnd = False    
    words.append(word)

if rule_length and rule_2time and rule_startEnd:
    print('Yes')
else:
    print('No')    

