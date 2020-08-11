# HonestOrUnkind2
# input
N = int(input())
maxlen = len(bin(2**N-1)[2:])
testimonies = []
res = 0

for i in range(N):
    testimony = [-1] * N
    n = int(input())
    
    for j in range(n):
        x, y = map(int, input().split())
        testimony[x-1] = y

    testimonies.append(testimony)

for _ in range(1 << N):
    # 仮定とした正直者と，仮定とした正直者の証言を比較すれば十分であることに注意(仮定により，どうあるべきかは決まっているので)
    ok = True
    ans = [int(e) for e in bin(_)[2:].zfill(maxlen)]
    for i, t in enumerate(ans.copy()):
        if t==1: # 正直者の仮定により証言を検証
            for j, v in enumerate(testimonies[i]):
                if v != -1: # -1は言及なし
                    if ans[j] == -1:
                        ans[j] = v 
                    elif ans[j] != v:
                        ok = False
    # print('modified ans: ', ans)
    if ok:
        # print('here')
        res = max(res, sum(e for e in ans if e==1))
    
    
# output
print(res)
