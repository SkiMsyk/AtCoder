# 0,...,n-1,について並び替えn!を列挙
# 列挙する部分
def make_sequence(pos, n, used):
    res_make_sequence = []
    for i in range(n):
        if pos != i and used[i]:
            res_make_sequence.append(i)
            used[i] = False
    return res_make_sequence


def permutation(pos, n):
    used = [True]*pos # 列挙済みフラグ
    res_permutation = []
    while sum(used) != 0:
        res_permutation.append(make_sequence(pos, n, used))
    return res_permutation