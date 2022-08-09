def Daydream(S):
    T = ''
    if len(S) < 5:
        return 'NO'
    else:
        pos = 0
        while len(T) < len(S):
            if pos + 11 <= len(S) and 'dreameraser' == S[pos:pos+11]:
                T += 'dreameraser'
                pos += 11
            elif pos + 10 <= len(S) and 'dreamerase' == S[pos:pos+10]:
                T += 'dreamerase'
                pos += 10
            elif pos + 7 <= len(S) and 'dreamer' == S[pos:pos+7]:
                T += 'dreamer'
                pos += 7
            elif pos + 5 <= len(S) and 'dream' == S[pos:pos+5]:
                T += 'dream'
                pos += 5
            elif pos + 6 <= len(S) and 'eraser' == S[pos:pos+6]:
                T += 'eraser'
                pos += 6
            elif pos + 5 <= len(S) and 'erase' == S[pos:pos+5]:
                T += 'erase'
                pos += 5
            else:
                break
    if S == T:
        return 'YES'
    else:
        return 'NO'

def main():
    S = input()
    res = Daydream(S)
    print(res)

main()