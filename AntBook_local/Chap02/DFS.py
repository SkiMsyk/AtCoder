# let a1, a2, ..., an are integer
# Determine if the sum can be just k
n = int(input())
a = list(map(int, input().split()))
k = int(input())

def dfs(i, s):
    if i == n:
        # i == n is True -> return k
        # iがnなら，つまり全ての和である場合はkと一致するかを返す
        return s == k
    if dfs(i+1, s):
        # i != n and dfs(i+1, s) == True -> return True
        # iがn出ない時，かつdfs(i+1, s)がTrueである時はTrueを返す
        # 和がkと一致した時はここ
        return True
    if dfs(i+1, s + a[i]):
        # i != n and dfs(i+1, s) != True and dfs(i+1, s+a[i]) == True -> return True
        # dfs(i+1, s+a[i])，sにa[i]を足した時，a+
        return True
    # else return False 
    return False

if dfs(0, 0):
    print("Yes")
else:
    print("No")
